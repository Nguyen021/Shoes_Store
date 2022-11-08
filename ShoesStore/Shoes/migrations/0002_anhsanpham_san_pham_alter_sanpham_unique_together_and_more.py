# Generated by Django 4.1.2 on 2022-10-08 03:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shoes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='anhsanpham',
            name='san_pham',
            field=models.ForeignKey(blank=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Shoes.sanpham'),
        ),
        migrations.AlterUniqueTogether(
            name='sanpham',
            unique_together={('ten', 'danh_muc')},
        ),
        migrations.CreateModel(
            name='BinhLuan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ngay_tao', models.DateTimeField(auto_now_add=True)),
                ('ngay_sua', models.DateTimeField(auto_now=True)),
                ('noi_dung', models.TextField()),
                ('nguoi_tao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('san_pham', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shoes.sanpham')),
            ],
            options={
                'db_table': 'BinhLuan',
            },
        ),
    ]
