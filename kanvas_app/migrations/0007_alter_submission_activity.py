# Generated by Django 3.2.6 on 2021-08-09 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kanvas_app', '0006_auto_20210809_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='kanvas_app.activity'),
        ),
    ]
