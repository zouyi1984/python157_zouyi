# coding=gbk
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "baizhi.settings")
django.setup()
from mainapp.models import TCategory,TBook
#
# book_name = "˵����"
# dangdang_price =  57.30
# market_price = 70.00
# sales = 498
# storage =  2000
# editer_commond = 22
# anthor = "������"
# category = 25
# pics = "27855329-1_u_4.jpg"
# c_introduce = '''��˵���Ρ��Է������徫�񡢼�������ΪĿ�ģ����������δӡ�����֮�ѡ�������ɽ������151�����Ҫ����ʷ�¼����������������������������ÿ͹�ʷʵ���������β��ܸ�����*��������ԭ�򡣱���*�������ڡ���������������1965����̨��ƽԭ��������棬���ԡ�����ƫ����Ӱ��̨����Ȩ���ǵý���ʯ��ŭ��ȫ��ӡ��Ʒ��������١��˴γ��������ݵİ汾����������֮���������Թ��񵳡����빤���ռǡ�֮���ܵ�����Ѱ��ģ�ԭԭ�����س��ֳ����꽯��ʯ���Ļ���������۹ܿص�һ���¼���'''
# n_introduce = '''�����������������룬����������ˣ�����֪�����ˡ����ԡ�һҶ�����������ȱ���Ϊ������̸����������׫�ģ���Ʒ���ᡣ1924�괴�졶����������������֪�����絳�������ž�۽���������絳��1951�굽̨�塣
#
# ����������ϵ������֮�ӡ�̨������������������20����70��90���Ϊ̨�塶�й�ʱ�������ߣ��־����������ݡ�1970��9��2�գ������Ᵽ������ͻ�𣬡��й�ʱ�����ɳ�4λ�¸Ҽ��߸�����̨�ǵ�����������������֮һ��'''
# TBook.objects.create(book_name=book_name,dangdang_price=dangdang_price,market_price=market_price,sales=sales,
#                 storage=storage,editer_commond=editer_commond,anthor=anthor,category_id=category,pics=pics,
#                      c_introduce=c_introduce,n_introduce=n_introduce)
# TBook.objects.create(book_name=book_name,dangdang_price=dangdang_price,market_price=market_price,sales=sales,
#                 storage=storage,editer_commond=editer_commond,anthor=anthor,category_id=category,pics=pics,
#                      c_introduce=c_introduce,n_introduce=n_introduce)