# Generated by Django 3.1 on 2020-09-13 10:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cafepages', '0002_auto_20200906_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='College',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.CreateModel(
            name='contactform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lname', models.CharField(blank=True, max_length=10)),
                ('subject', models.CharField(blank=True, max_length=10)),
                ('email', models.EmailField(blank=True, max_length=10)),
                ('message', models.CharField(blank=True, max_length=1000)),
                ('fname', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]