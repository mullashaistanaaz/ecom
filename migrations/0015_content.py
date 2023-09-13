# Generated by Django 4.2.4 on 2023-09-07 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_customersupport'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('content_type', models.CharField(choices=[('Article', 'Article'), ('ProductDescription', 'Product Description'), ('BlogPost', 'Blog Post'), ('FAQ', 'FAQ')], max_length=20)),
                ('body', models.TextField()),
                ('published_at', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]