# Generated by Django 4.2.13 on 2024-05-22 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tilda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublishedPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(help_text='E.g.: /my-landing/mobile/', max_length=200, verbose_name='Public path to page')),
                ('is_enabled', models.BooleanField(default=True, verbose_name='Is published')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Note')),
                ('tilda_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tilda.tildapage', verbose_name='Tilda page')),
            ],
            options={
                'unique_together': {('path', 'is_enabled')},
            },
        ),
    ]
