# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TAddress(models.Model):
    recever = models.CharField(max_length=40,  null=True)       #地址
    receve_address = models.CharField(max_length=40,  null=True)    #详细地址
    zip_code = models.CharField(max_length=6,  null=True)       #邮编
    tel = models.CharField(max_length=40,  null=True)       #电话
    phone = models.CharField(max_length=40,  null=True)     #手机
    user = models.ForeignKey('TUser', models.CASCADE,  null=True)    #关联用户
    class Meta:
        db_table = 't_address'


class TBook(models.Model):
    book_name = models.CharField(max_length=40,  null=True)     #书名
    dangdang_price = models.FloatField(null=True)       #当当价格
    market_price = models.FloatField(null=True)         #原价
    sales = models.IntegerField(null=True)     #销售多少
    storage = models.IntegerField(null=True)   #库存
    pushish_time = models.DateField(null=True,auto_now_add=True)      #第一次添加时间
    editer_commond = models.IntegerField(null=True)        #编辑
    anthor = models.CharField(max_length=40,  null=True)        #作者
    category = models.ForeignKey('TCategory', models.CASCADE,  null=True)    #关联2级分类ID
    pics = models.CharField(max_length=100, null=True)      #图片
    c_introduce = models.TextField(null=True)       #内容简介
    n_introduce = models.TextField(null=True)       #作者简介
    directory = models.IntegerField(null=True)    #页数
    class Meta:
        db_table = 't_book'


class TCategory(models.Model):
    category_name = models.CharField(max_length=40,  null=True)     #书类
    parent_id = models.IntegerField(null=True)          #书类关联ID
    class Meta:

        db_table = 't_category'


class TOrder(models.Model):
    book_name = models.CharField(max_length=40,null=True)
    order_price = models.FloatField(null=True)          #订单价格
    create_time = models.DateTimeField(null=True,auto_now_add=True)       #生成订单时间
    order_id = models.IntegerField(null=True)           #订单编报
    user = models.ForeignKey('TUser', models.CASCADE,  null=True)        #关联用户ID
    receive_address = models.CharField(max_length=40,  null=True)   #接受地址
    book_id = models.IntegerField(null=True)
    count = models.IntegerField(null=True)
    class Meta:
        db_table = 't_order'


class TOrderitem(models.Model):     #订单项表
    book_name = models.CharField(max_length=40,  null=True)     #书名
    sub_total = models.FloatField(null=True)    #总价格
    order = models.ForeignKey(TOrder, models.CASCADE,  null=True)    #订单
    book = models.ForeignKey(TBook, models.CASCADE,  null=True)      #书名
    class Meta:
        db_table = 't_orderitem'


class TUser(models.Model):
    email = models.CharField(max_length=40,  null=True)     #邮箱
    username = models.CharField(max_length=40,  null=True)      #昵称
    password = models.CharField(max_length=80,  null=True)      #密码
    status = models.IntegerField(null=True,default=0)        #状态
    class Meta:
        db_table = 't_user'


class Confirm_string(models.Model):
    code = models.CharField(max_length=256,verbose_name="用户注册码")
    email = models.CharField(max_length=40,null=True)
    code_time = models.DateTimeField(null=True,auto_now_add=True)
    user = models.ForeignKey("TUser",on_delete=models.CASCADE,verbose_name="关联用户",null=True)
    class Meta:
        db_table = 't_confirm_string'




