# Generated by Django 2.2 on 2019-07-11 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendence', '0007_auto_20190712_0332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='t_id',
            field=models.IntegerField(default=1),
        ),
    ]