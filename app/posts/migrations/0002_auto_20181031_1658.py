# Generated by Django 2.1.2 on 2018-10-31 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-pk'], 'verbose_name': '포스트', 'verbose_name_plural': '포스트 목록'},
        ),
    ]
