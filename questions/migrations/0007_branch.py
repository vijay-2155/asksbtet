# Generated by Django 4.2.5 on 2023-10-04 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_answer_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('short_form', models.CharField(max_length=10)),
            ],
        ),
    ]
