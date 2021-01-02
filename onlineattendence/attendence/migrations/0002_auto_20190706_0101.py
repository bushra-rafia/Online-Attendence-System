# Generated by Django 2.2 on 2019-07-05 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendence', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_code', models.CharField(max_length=10)),
                ('Title', models.CharField(max_length=100)),
                ('Semister', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='teacher',
            name='t_id',
            field=models.IntegerField(default=''),
        ),
        migrations.CreateModel(
            name='Teaches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_code', models.ForeignKey(on_delete='CASCADE', to='attendence.Course')),
                ('t_id', models.ForeignKey(on_delete='CASCADE', to='attendence.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Attendence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Section', models.CharField(max_length=10)),
                ('Course_code', models.ForeignKey(on_delete='CASCADE', to='attendence.Course')),
                ('t_id', models.ForeignKey(on_delete='CASCADE', to='attendence.teacher')),
            ],
        ),
    ]
