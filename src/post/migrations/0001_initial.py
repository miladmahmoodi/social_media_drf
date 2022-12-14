# Generated by Django 4.1 on 2022-08-11 05:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import post.models.post


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tag', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Time')),
                ('caption', models.TextField(verbose_name='Caption')),
                ('file', models.ImageField(blank=True, max_length=128, null=True, upload_to=post.models.post.get_file_path, verbose_name='Media')),
                ('reshare_count', models.PositiveIntegerField(default=0, verbose_name='Total Count')),
                ('comment_count', models.PositiveIntegerField(default=0, verbose_name='Total Comment')),
                ('like_count', models.PositiveIntegerField(default=0, verbose_name='Total Like')),
                ('feed', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Feed')),
                ('like', models.ManyToManyField(blank=True, related_name='likers', to=settings.AUTH_USER_MODEL, verbose_name='Like')),
                ('reshare', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reshares', to='post.post', verbose_name='Feed')),
                ('tag', models.ManyToManyField(blank=True, to='tag.tag', verbose_name='Tag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Time')),
                ('text', models.TextField(verbose_name='Text')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='post.post', verbose_name='Parent')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Post', to='post.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
