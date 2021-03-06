# Generated by Django 3.1 on 2020-08-30 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Phone', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Phone', models.CharField(max_length=255)),
                ('Email', models.EmailField(max_length=254, null=True)),
                ('Status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('Not verified', 'Not verified')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255, null=True)),
                ('Discription', models.TextField(max_length=1024, null=True)),
                ('StartDate', models.DateField()),
                ('EndDate', models.DateField()),
                ('Price', models.IntegerField(null=True)),
                ('Image', models.CharField(max_length=1024, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255, null=True)),
                ('Destinations', models.TextField(max_length=255, null=True)),
                ('DateStarted', models.DateField(null=True)),
                ('DateCompleated', models.DateField(null=True)),
                ('Expences', models.IntegerField(null=True)),
                ('Profit', models.IntegerField(null=True)),
                ('Branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='NesaraTours.branch')),
                ('Client', models.ManyToManyField(null=True, to='NesaraTours.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255, null=True)),
                ('Phone', models.CharField(max_length=255, null=True)),
                ('Email', models.EmailField(max_length=254, null=True)),
                ('Sal', models.CharField(max_length=10, null=True)),
                ('branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='NesaraTours.branch')),
            ],
        ),
    ]
