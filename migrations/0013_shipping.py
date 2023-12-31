# Generated by Django 4.2.4 on 2023-09-07 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_userpurchasehistory_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carrier', models.CharField(max_length=100)),
                ('tracking_number', models.CharField(max_length=50)),
                ('shipping_date', models.DateTimeField()),
                ('estimated_delivery_date', models.DateTimeField()),
                ('status', models.CharField(choices=[('Shipped', 'Shipped'), ('Out for Delivery', 'Out for Delivery'), ('Delivered', 'Delivered'), ('Delayed', 'Delayed')], max_length=20)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.order')),
            ],
        ),
    ]
