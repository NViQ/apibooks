# Generated by Django 4.2 on 2023-04-29 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apilib', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authors',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='authors',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='books',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
