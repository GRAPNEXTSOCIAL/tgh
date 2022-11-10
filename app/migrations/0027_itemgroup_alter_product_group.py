# Generated by Django 4.0.4 on 2022-11-08 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_alter_tax_tax_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Itemgroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_group_code', models.IntegerField()),
                ('item_group_name', models.CharField(max_length=50)),
                ('item_group_description', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.itemgroup'),
        ),
    ]
