# Generated by Django 3.0.3 on 2020-03-20 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
