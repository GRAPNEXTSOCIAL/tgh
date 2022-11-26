# Generated by Django 4.0.4 on 2022-11-25 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_paymentmode'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='bill_type',
            field=models.CharField(choices=[('SGST/CGST', 'SGST/CGST'), ('IGST', 'IGST'), ('UNREGD', 'UNREGD'), ('COMPOSITE', 'COMPOSITE')], default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchase',
            name='gstin',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
