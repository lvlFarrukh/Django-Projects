# Generated by Django 3.0.3 on 2020-03-20 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20200320_0335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='banner_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
