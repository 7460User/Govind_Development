# Generated by Django 4.1.4 on 2023-09-04 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmpDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=101)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=60)),
                ('state', models.CharField(max_length=50)),
                ('zip', models.IntegerField(max_length=20)),
            ],
        ),
    ]
