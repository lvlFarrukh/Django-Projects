# Generated by Django 3.0.3 on 2020-04-03 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='cinc',
            new_name='cnic',
        ),
    ]
