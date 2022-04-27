# Generated by Django 4.0.4 on 2022-04-26 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='img1',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='img2',
        ),
    ]