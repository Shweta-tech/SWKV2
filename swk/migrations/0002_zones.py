# Generated by Django 3.1.1 on 2020-12-16 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swk', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zone_name', models.CharField(blank=True, max_length=100, null=True)),
                ('zone_id', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'zones',
                'managed': False,
            },
        ),
    ]
