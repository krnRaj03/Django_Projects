# Generated by Django 4.0.5 on 2022-08-26 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('startdate', models.DateField(null=True)),
                ('enddate', models.DateField(null=True)),
            ],
        ),
    ]