# Generated by Django 4.2.4 on 2023-09-07 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_category_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catelog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='catelog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.catelog'),
        ),
    ]
