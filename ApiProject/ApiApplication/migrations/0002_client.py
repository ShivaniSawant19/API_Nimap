# Generated by Django 4.2.1 on 2023-05-06 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiApplication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('client_name', models.CharField(max_length=200)),
                ('created_at', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
