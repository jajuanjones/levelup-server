# Generated by Django 4.0.4 on 2022-04-27 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='gamer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='levelupapi.gamer'),
        ),
        migrations.AlterField(
            model_name='game',
            name='maker',
            field=models.CharField(max_length=20),
        ),
    ]
