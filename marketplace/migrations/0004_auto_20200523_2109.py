# Generated by Django 3.0.5 on 2020-05-23 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0003_imagemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(upload_to='uploads/product/%Y/%m/%d/')),
            ],
        ),
        migrations.DeleteModel(
            name='ImageModel',
        ),
    ]
