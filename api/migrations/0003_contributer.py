# Generated by Django 3.2.8 on 2021-10-31 22:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_todo_creator'),
    ]

    operations = [
        migrations.CreateModel(
            name='contributer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contributeing_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('todo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.todo')),
            ],
        ),
    ]
