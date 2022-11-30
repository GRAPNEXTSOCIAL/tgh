# Generated by Django 4.0.4 on 2022-11-30 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_purchaseproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inv_date', models.DateField(blank=True)),
                ('inv_no', models.CharField(max_length=100)),
                ('total_qty', models.FloatField(null=True)),
                ('total_amt', models.FloatField(null=True)),
                ('discount', models.FloatField(null=True)),
                ('gst_amt', models.FloatField(null=True)),
                ('grand_total', models.FloatField(null=True)),
                ('by_cash', models.FloatField(default=0.0, null=True)),
                ('by_card', models.FloatField(default=0.0, null=True)),
                ('by_credit', models.FloatField(default=0.0, null=True)),
                ('sdx_fin', models.FloatField(default=0.0, null=True)),
                ('by_upi', models.FloatField(default=0.0, null=True)),
                ('redeem', models.FloatField(default=0.0, null=True)),
                ('ct_amt', models.FloatField(default=0.0, null=True)),
                ('refund', models.FloatField(default=0.0, null=True)),
            ],
        ),
    ]
