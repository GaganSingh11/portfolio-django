# Generated by Django 4.0.4 on 2022-04-26 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('subject', models.CharField(blank=True, max_length=200, null=True)),
                ('body', models.TextField()),
            ],
        ),
    ]
