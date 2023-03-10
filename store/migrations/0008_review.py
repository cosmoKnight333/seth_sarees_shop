# Generated by Django 4.1.3 on 2022-12-26 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_contact_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('reviewer_name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('back_link', models.TextField(blank=True, default='', null=True)),
            ],
        ),
    ]
