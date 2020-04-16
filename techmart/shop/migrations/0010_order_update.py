# Generated by Django 3.0.3 on 2020-04-08 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20200403_1157'),
    ]

    operations = [
        migrations.CreateModel(
            name='order_update',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField()),
                ('email', models.EmailField(default='', max_length=254)),
                ('update_description', models.CharField(default='', max_length=500)),
                ('update_time', models.TimeField(auto_now=True)),
            ],
        ),
    ]
