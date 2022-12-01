# Generated by Django 4.0.4 on 2022-12-01 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_color_item_color_alter_product_item_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cess',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='gst',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='hsn_no',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='tax_on',
            field=models.CharField(default='BASIC', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='purchase_tax_type',
            field=models.CharField(choices=[('CGST', 'CGST'), ('SGST', 'SGST'), ('IGST', 'IGST'), ('UNREGD', 'UNREGD'), ('COMPOSITE', 'COMPOSITE')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='bill_type',
            field=models.CharField(choices=[('CGST', 'CGST'), ('SGST', 'SGST'), ('IGST', 'IGST'), ('UNREGD', 'UNREGD'), ('COMPOSITE', 'COMPOSITE')], max_length=50),
        ),
    ]
