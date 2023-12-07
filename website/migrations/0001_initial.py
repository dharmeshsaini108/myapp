# Generated by Django 4.2.3 on 2023-07-28 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('college', models.CharField(max_length=200)),
                ('age', models.IntegerField(max_length=10)),
                ('isActive', models.BooleanField(default=False)),
            ],
        ),
    ]
