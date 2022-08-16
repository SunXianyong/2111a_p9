from django.db import models


class Address(models.Model):
    class Meta:
        db_table = "address"

    choices = (
        (0, "男"),
        (1, "女"),
    )

    use_name = models.CharField(max_length=32, verbose_name="收件人名字")
    use_phone = models.CharField(max_length=11, verbose_name="收件人手机")
    use_gender = models.IntegerField(default=0, verbose_name="性别")
    address = models.CharField(max_length=128, verbose_name="收货地址")
    address_detailed = models.CharField(max_length=128, verbose_name="收货地址具体位置")
    title = models.CharField(max_length=16, default="", verbose_name="标签")
    longitude = models.DecimalField(max_digits=10, decimal_places=6, verbose_name="经度")
    latitude = models.DecimalField(max_digits=10, decimal_places=6, verbose_name="纬度")
    user_id = models.IntegerField(verbose_name="关联用户id")
    merchant_id = models.IntegerField(verbose_name="关联商家id")


class Merchant(models.Model):
    name = models.CharField(max_length=32, verbose_name="店铺名称")
    logo = models.CharField(max_length=1024, verbose_name="图片")
    info = models.CharField(max_length=2048, verbose_name="描述")
    money = models.IntegerField(default=0, verbose_name="起送费")

    class Meta:
        db_table = "merchant"


class User(models.Model):
    name = models.CharField(max_length=32, verbose_name="用户名")
    logo = models.CharField(max_length=1024, verbose_name="头像")
    info = models.CharField(max_length=2048, verbose_name="描述")
    phone = models.CharField(max_length=11, verbose_name="收件人手机")
    identity = models.CharField(max_length=18, verbose_name="身份证")
    gender = models.IntegerField(default=0, verbose_name="性别")
    password = models.CharField(max_length=512, verbose_name="密码")
    merchant = models.BooleanField(default=False, verbose_name="商家开关")
    rider = models.BooleanField(default=False, verbose_name="骑手开关")
    user = models.BooleanField(default=True, verbose_name="订餐权限")
    staff = models.BooleanField(default=False, verbose_name="员工权限")
    merchant_id = models.IntegerField(default=0, verbose_name="关联商家id")

    class Meta:
        db_table = "user"
