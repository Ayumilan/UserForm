# Generated by Django 4.1.7 on 2023-05-21 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Dob', models.DateField()),
                ('Email', models.EmailField(max_length=254)),
                ('Mobile', models.CharField(max_length=10)),
            ],
        ),
    ]
