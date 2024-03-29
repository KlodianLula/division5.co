# Generated by Django 3.1 on 2020-08-17 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orderable5', '0003_auto_20200813_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='group_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='orderable5.articlegroup'),
        ),
        migrations.AlterField(
            model_name='orderablestorearticles',
            name='article_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='orderable5.article'),
        ),
        migrations.AlterField(
            model_name='orderablestorearticles',
            name='store_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stores', to='orderable5.store'),
        ),
    ]
