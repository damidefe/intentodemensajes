# Generated by Django 4.1 on 2022-09-28 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlogs', '0009_alter_blog_fecha_posteo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='id_blog',
            field=models.IntegerField(null=True),
        ),
    ]