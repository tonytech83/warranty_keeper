# Generated by Django 5.1.1 on 2024-10-06 11:26

import django.core.validators
import django.db.models.deletion
import warranty_keeper.warranties.validators
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('suppliers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Warranty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2)])),
                ('description', models.TextField(blank=True, null=True)),
                ('invoice_img', models.FileField(blank=True, null=True, upload_to='invoices/', validators=[warranty_keeper.warranties.validators.validate_mime_type])),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='suppliers.supplier')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
