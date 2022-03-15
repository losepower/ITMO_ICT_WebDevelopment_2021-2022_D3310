# Generated by Django 4.0.3 on 2022-03-07 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('birthday', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=240)),
                ('Type', models.CharField(max_length=100)),
                ('year_of_pub', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library_app.author')),
            ],
            options={
                'ordering': ['book_name'],
            },
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('sex', models.CharField(choices=[('m', 'man'), ('w', 'woman')], max_length=1)),
                ('birthday', models.DateField()),
                ('passport', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=False)),
                ('id_book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='library_app.book')),
            ],
        ),
    ]
