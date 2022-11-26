# Generated by Django 4.0.4 on 2022-11-23 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('by_cash', models.FloatField(default=0, null=True)),
                ('by_card', models.FloatField(default=0, null=True)),
                ('by_credit', models.FloatField(default=0, null=True)),
                ('sdx_fin', models.FloatField(default=0, null=True)),
                ('by_upi', models.FloatField(default=0, null=True)),
            ],
        ),
    ]
