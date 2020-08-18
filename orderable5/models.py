from django.db import models
from django.contrib.postgres.fields import ArrayField


# ArticleGroup ( Id, name )
class ArticleGroup(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name 


# Article ( Id, name, group_id )
class Article(models.Model):
    name = models.CharField(max_length=50)
    group_id = models.ForeignKey(ArticleGroup, related_name="articles", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# ArticleAggregation ( Id agg_article_id, article_id )
class ArticleAggregation(models.Model):
    article_id = models.ForeignKey(
        Article, 
        related_name='article_id',
        on_delete=models.CASCADE
    )
    agg_article_id = models.ManyToManyField(
        Article,
        related_name='agg_article_id'
        #on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.article_id)


# Store ( Id, name )
class Store(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# OrderableStoreArticles ( Id, store_id, article_id, date )
class OrderableStoreArticles(models.Model):
    store_id = models.ForeignKey(Store, related_name="stores", on_delete=models.CASCADE)
    article_id = models.ForeignKey(Article,  related_name="articles", on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.article_id)


# Order ( Id, store_id, date )
class Order(models.Model):
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    date = models.DateField()


# OrderItems ( Id, order_id, ordere_amount )
class OrderItems(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    order_amount = models.IntegerField()


# Division5 Task - qyery model
class Division5(models.Model):	
    group_id = models.IntegerField()
    group_name = models.CharField(max_length=50)
    artikull_id = models.IntegerField(db_column='artikull_id', primary_key=True)
    artikull_name = models.CharField(db_column='artikull_bije', max_length=50)
    artikull_prind = models.CharField(db_column='artikull_prind_optional', max_length=50)
    