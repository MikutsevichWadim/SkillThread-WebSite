# Generated by Django 5.1.4 on 2024-12-30 00:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tests_tests', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='testattempt',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_attempts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='testresult',
            name='test_attempt',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tests_tests.testattempt'),
        ),
    ]
