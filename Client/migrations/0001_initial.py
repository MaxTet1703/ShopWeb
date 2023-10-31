# Generated by Django 3.2 on 2023-10-17 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, verbose_name='Название раздела')),
            ],
            options={
                'verbose_name': 'Сатегории',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Название товара')),
                ('description', models.TextField(blank=True, verbose_name='Описание товара')),
                ('price', models.IntegerField(verbose_name='Цена за товар')),
                ('image', models.ImageField(upload_to='menu/', verbose_name='Внешний вид товара')),
                ('type_of_position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Client.chapter')),
            ],
            options={
                'verbose_name': 'Меню',
                'verbose_name_plural': 'Меню',
            },
        ),
    ]
