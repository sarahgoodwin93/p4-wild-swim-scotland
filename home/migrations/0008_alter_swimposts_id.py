# Generated by Django 4.2.8 on 2024-01-19 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_swimposts_description_alter_swimposts_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='swimposts',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]