# Generated by Django 2.2 on 2019-05-02 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100, null=True)),
                ('event_type', models.CharField(max_length=50, null=True)),
                ('location', models.CharField(max_length=50, null=True)),
                ('date', models.CharField(max_length=100, null=True)),
                ('fees', models.IntegerField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('event_details', models.CharField(max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'Create Event',
                'db_table': 'create_event',
            },
        ),
    ]