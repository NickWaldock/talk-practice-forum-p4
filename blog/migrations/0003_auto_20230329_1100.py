# Generated by Django 3.2.18 on 2023-03-29 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=100)),
                ('subject', models.TextField(max_length=100)),
                ('message', models.TextField()),
                ('member', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
    ]
