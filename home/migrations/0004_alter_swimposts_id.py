# Generated by Django 4.2.8 on 2024-01-14 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_review_swimposts_created_on_swimposts_updated_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='swimposts',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
