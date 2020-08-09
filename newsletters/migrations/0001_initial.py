# Generated by Django 2.2.14 on 2020-08-09 01:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=django.utils.timezone.now)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=500)),
                ('target', models.IntegerField()),
                ('frequency', models.CharField(max_length=200)),
            ],
        ),
    ]
