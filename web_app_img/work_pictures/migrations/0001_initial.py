# Generated by Django 4.1.3 on 2023-05-31 21:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Icom_format_st',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='Chefs/static/icons')),
                ('base64', models.TextField(blank=True)),
                ('icon_75', models.ImageField(blank=True, null=True, upload_to='Chefs/static/icons')),
                ('icon_50', models.ImageField(blank=True, null=True, upload_to='Chefs/static/icons')),
                ('icon_25', models.ImageField(blank=True, null=True, upload_to='Chefs/static/icons')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Користувач')),
            ],
        ),
    ]
