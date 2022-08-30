# Generated by Django 4.1 on 2022-08-22 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('use_name', models.CharField(max_length=32, verbose_name='收件人名字')),
                ('use_phone', models.CharField(max_length=11, verbose_name='收件人手机')),
                ('use_gender', models.IntegerField(default=0, verbose_name='性别')),
                ('address', models.CharField(max_length=128, verbose_name='收货地址')),
                ('address_detailed', models.CharField(max_length=128, verbose_name='收货地址具体位置')),
                ('title', models.CharField(default='', max_length=16, verbose_name='标签')),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=10, verbose_name='经度')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=10, verbose_name='纬度')),
                ('user_id', models.IntegerField(verbose_name='关联用户id')),
                ('merchant_id', models.IntegerField(verbose_name='关联商家id')),
            ],
            options={
                'db_table': 'address',
            },
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='店铺名称')),
                ('logo', models.CharField(max_length=1024, verbose_name='图片')),
                ('info', models.CharField(max_length=2048, verbose_name='描述')),
                ('money', models.IntegerField(default=0, verbose_name='起送费')),
            ],
            options={
                'db_table': 'merchant',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('uuid', models.IntegerField(primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='用户名')),
                ('logo', models.CharField(max_length=1024, verbose_name='头像')),
                ('info', models.CharField(max_length=2048, verbose_name='描述')),
                ('phone', models.CharField(max_length=11, verbose_name='收件人手机')),
                ('identity', models.CharField(max_length=18, verbose_name='身份证')),
                ('gender', models.IntegerField(default=0, verbose_name='性别')),
                ('password', models.CharField(max_length=512, verbose_name='密码')),
                ('merchant', models.BooleanField(default=False, verbose_name='商家开关')),
                ('rider', models.BooleanField(default=False, verbose_name='骑手开关')),
                ('user', models.BooleanField(default=True, verbose_name='订餐权限')),
                ('staff', models.BooleanField(default=False, verbose_name='员工权限')),
                ('merchant_id', models.IntegerField(default=0, verbose_name='关联商家id')),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='VegetableLabel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='标签名')),
                ('ord_id', models.IntegerField(default=0)),
                ('combo', models.BooleanField(default=0, verbose_name='套餐')),
                ('merchant', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='label', to='app.merchant')),
            ],
            options={
                'ordering': ['-combo', '-ord_id'],
            },
        ),
        migrations.CreateModel(
            name='Vegetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='菜名')),
                ('money', models.IntegerField(default=0, verbose_name='菜价格')),
                ('logo', models.CharField(max_length=1024, verbose_name='图片')),
                ('label', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vegetable', to='app.vegetablelabel')),
                ('merchant', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='app.merchant')),
                ('order', models.ManyToManyField(related_name='order', through='app.Order', to='app.user')),
            ],
            options={
                'ordering': ['label'],
            },
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='vegetable', to='app.user'),
        ),
        migrations.AddField(
            model_name='order',
            name='vegetable',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='app.vegetable'),
        ),
    ]
