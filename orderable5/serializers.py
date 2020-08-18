from rest_framework import serializers
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


class ArticleSerializer(serializers.HyperlinkedModelSerializer): #ModelSerializer
    class Meta:
        model = Article
        fields = ('id', 'url', 'name', 'group_id')


class ArticleGroupSerializer(serializers.HyperlinkedModelSerializer): #ModelSerializer
    articles = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = ArticleGroup
        fields = ('id', 'url', 'name', 'articles')


class StoreSerializer(serializers.HyperlinkedModelSerializer): #ModelSerializer
    stores = serializers.StringRelatedField(many=True)
    class Meta:
        model = Store
        fields = ('id', 'url', 'name', 'stores')                


class ArticleAggregationSerializer(serializers.HyperlinkedModelSerializer): #ModelSerializer
    class Meta:
        model = ArticleAggregation
        fields = ('id', 'url', 'article_id', 'agg_article_id')


class OrderableStoreArticlesSerializer(serializers.HyperlinkedModelSerializer): #ModelSerializer
    class Meta:
        model = OrderableStoreArticles
        fields = ('id', 'url', 'store_id', 'article_id', 'date') #, 'articles')   


class OrderSerializer(serializers.HyperlinkedModelSerializer): #ModelSerializer
    class Meta:
        model = Order
        fields = ('id', 'url', 'store_id', 'date')
  
class OrderItemsSerializer(serializers.HyperlinkedModelSerializer): #ModelSerializer
    class Meta:
        model = OrderItems
        fields = ('id', 'url', 'order_id', 'order_amount')


class Division5Serializer(serializers.HyperlinkedModelSerializer): #ModelSerializer
    class Meta:
        model = Division5
        fields = ('group_id', 'url', 'group_name', 'artikull_id', 'artikull_prind')   
