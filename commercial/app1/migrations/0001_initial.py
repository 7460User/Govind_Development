# Generated by Django 4.1.4 on 2023-08-02 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.CharField(max_length=120)),
                ('phone', models.IntegerField(max_length=12)),
                ('desc', models.CharField(max_length=50)),
                ('date', models.DateField()),
            ],
        ),
    ]