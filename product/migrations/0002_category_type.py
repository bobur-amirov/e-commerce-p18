# Generated by Django 5.0.6 on 2024-05-24 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='type',
            field=models.IntegerField(choices=[(0, 'Non_type'), (1, 'Clothes'), (2, 'Food')], default=0),
        ),
    ]
