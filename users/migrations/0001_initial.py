# Generated by Django 3.1.2 on 2020-12-26 22:34

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
                ('login', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('weight', models.IntegerField(default=0)),
                ('height', models.IntegerField(default=0)),
                ('sex', models.BooleanField(default=True)),
                ('calories', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='userdetails', serialize=False, to='users.user')),
            ],
        ),
    ]