# Generated by Django 4.0.6 on 2022-11-13 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dreamit', '0003_chapters'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ch_name', models.CharField(default='', max_length=100)),
                ('image', models.ImageField(default='', upload_to='dreamit/image')),
            ],
        ),
    ]