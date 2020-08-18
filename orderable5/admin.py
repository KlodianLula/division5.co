from django.contrib import admin
from . models import (
                Article, 
                ArticleGroup, 
                ArticleAggregation, 
                Store, 
                Order,
                OrderItems,
                OrderableStoreArticles
)

admin.site.register(Article)
admin.site.register(ArticleGroup)
admin.site.register(ArticleAggregation)
admin.site.register(Store)
admin.site.register(Order)
admin.site.register(OrderItems)
admin.site.register(OrderableStoreArticles)
