from django.shortcuts import render
from rest_framework import viewsets
from .models import (
                Article, 
                ArticleGroup, 
                Store, 
                ArticleAggregation, 
                OrderableStoreArticles, 
                Order, 
                OrderItems,
                Division5
)

from .serializers import (
                ArticleSerializer, 
                ArticleGroupSerializer, 
                StoreSerializer, 
                ArticleAggregationSerializer, 
                OrderableStoreArticlesSerializer, 
                OrderSerializer, 
                OrderItemsSerializer,
                Division5Serializer
)


class ArticleGroupView(viewsets.ModelViewSet):
    queryset = ArticleGroup.objects.all()
    serializer_class = ArticleGroupSerializer    


class ArticleView(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleAggregationView(viewsets.ModelViewSet):
    queryset = ArticleAggregation.objects.all()
    serializer_class = ArticleAggregationSerializer


class StoreView(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer    


class OrderItemsView(viewsets.ModelViewSet):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializer


class OrderableStoreArticlesView(viewsets.ModelViewSet):
    queryset = OrderableStoreArticles.objects.all()
    serializer_class = OrderableStoreArticlesSerializer


class Division5View(viewsets.ModelViewSet):
    queryset = Division5.objects.raw('''
    WITH cte_one AS (
    SELECT 
        gr.id as group_id, 
        gr.name as group_name,
        art.id as artikull_id_prind,
        art.name as artikull_prind,
        agg.id as agg_clubed, 
        array_prepend(art.id, array_agg(agg_bija.article_id)) AS a_id
        
        FROM public.orderable5_articlegroup AS gr	
        left join public.orderable5_article as art
        on gr.id = art.group_id_id
        left join public.orderable5_articleaggregation as agg
        on art.id = agg.article_id_id 
        left join public.orderable5_articleaggregation_agg_article_id as agg_bija
        on agg.id = agg_bija.articleaggregation_id 
        --where  agg.article_id_id is not NULL
        group by gr.id, art.id, agg_clubed, agg_bija.articleaggregation_id
        order by gr.id, agg_bija.articleaggregation_id
    ),
    cte_two AS(
    SELECT 
            group_id, 
            group_name, 
            UNNEST((a_id)::int[]) as artikull_id,
            artikull_prind,
            artikull_id_prind
        from cte_one
        order by group_id, agg_clubed, artikull_id
    )
    SELECT
        group_id, 
        group_name, 
        artikull_id, 
        all_articles.name as artikull_bije, 
        artikull_prind as artikull_prind_optional
        
        FROM cte_two
            left join public.orderable5_article AS all_articles
            on all_articles.id = artikull_id
        where artikull_id_prind IN (
            select article_id_id from public.orderable5_orderablestorearticles
            where store_id_id = 1
            and date = '2020-08-18'
        )
        and artikull_id is not null
    ''')
    serializer_class = Division5Serializer
