from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('article-groups', views.ArticleGroupView)
router.register('articles', views.ArticleView)
router.register('article-agg', views.ArticleAggregationView)
router.register('stores', views.StoreView)
router.register('orders', views.OrderView)
router.register('order-items', views.OrderItemsView)
router.register('orderable-store-articles', views.OrderableStoreArticlesView)
router.register('division5-query', views.Division5View)

urlpatterns = [
    path('', include(router.urls))
]
