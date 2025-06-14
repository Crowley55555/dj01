# Generated by Django 5.2.2 on 2025-06-14 10:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='dislikes_count',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество дизлайков'),
        ),
        migrations.AddField(
            model_name='news',
            name='likes_count',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество лайков'),
        ),
        migrations.CreateModel(
            name='NewsReaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(verbose_name='IP адрес')),
                ('reaction', models.CharField(choices=[('like', 'Лайк'), ('dislike', 'Дизлайк')], max_length=7, verbose_name='Реакция')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата реакции')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reactions', to='news.news', verbose_name='Новость')),
            ],
            options={
                'verbose_name': 'Реакция на новость',
                'verbose_name_plural': 'Реакции на новости',
                'unique_together': {('news', 'ip_address')},
            },
        ),
    ]
