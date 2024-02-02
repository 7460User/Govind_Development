# Generated by Django 4.1.4 on 2023-02-20 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, null=True)),
                ('email', models.EmailField(max_length=50, null=True)),
                ('password', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]
