# Generated by Django 3.0.8 on 2020-07-15 06:58

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
            managers=[
                ('category_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('store_id', models.AutoField(primary_key=True, serialize=False)),
                ('store_name', models.CharField(max_length=255, unique=True)),
            ],
            managers=[
                ('store_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('barcode', models.BigIntegerField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=255, unique=True)),
                ('nutriscore_grade', models.CharField(max_length=4)),
                ('product_description', models.TextField()),
                ('off_url', models.CharField(max_length=255)),
                ('categories', models.ManyToManyField(to='core.Category')),
                ('stores', models.ManyToManyField(to='core.Store')),
                ('substitutes', models.ManyToManyField(to='core.Product')),
            ],
            managers=[
                ('product_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]