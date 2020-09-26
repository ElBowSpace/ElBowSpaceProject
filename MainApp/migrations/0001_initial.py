# Generated by Django 3.1.1 on 2020-09-26 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('active', models.BooleanField()),
                ('connection', models.ManyToManyField(related_name='_user_connection_+', to='MainApp.User')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('body', models.CharField(max_length=255)),
                ('time_stamp', models.DateTimeField()),
                ('image', models.TextField(max_length=255)),
                ('reply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.user')),
            ],
        ),
    ]
