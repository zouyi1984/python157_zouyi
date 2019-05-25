# coding=gbk
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "baizhi.settings")
django.setup()
from mainapp.models import TCategory,TBook
#
# book_name = "说南宋"
# dangdang_price =  57.30
# market_price = 70.00
# sales = 498
# storage =  2000
# editer_commond = 22
# anthor = "刘鄂公"
# category = 25
# pics = "27855329-1_u_4.jpg"
# c_introduce = '''《说南宋》以发扬忠义精神、激浊扬清为目的，叙述了南宋从“靖康之难”到“崖山覆亡”151年间重要的历史事件，对南宋历代君臣进行评述，用客观史实阐发了南宋不能复国、*终灭亡的原因。本书*初连载于《自立晚报》副刊，1965年由台湾平原出版社出版，因以“南宋偏安”影射台湾政权而惹得蒋介石大怒，全部印成品被查禁销毁。此次出版所依据的版本是由刘鄂公之子刘永宁自国民党《中央工作日记》之机密档案中寻获的，原原本本地呈现出当年蒋介石在文化界进行言论管控的一个事件。'''
# n_introduce = '''刘鄂公，本名刘家麟，湖北武昌县人，近代知名报人。曾以“一叶”“鄂公”等笔名为《自由谈》《华报》撰文，作品甚丰。1924年创办《汉报》。早年因受知于民社党创党人张君劢而加入民社党，1951年到台湾。
#
# 本书整理者系刘鄂公之子、台湾著名记者刘永宁。20世纪70—90年代为台湾《中国时报》记者，现居美国北加州。1970年9月2日，海内外保钓风云突起，《中国时报》派出4位勇敢记者赴钓鱼台登岛，刘永宁即是四人之一。'''
# TBook.objects.create(book_name=book_name,dangdang_price=dangdang_price,market_price=market_price,sales=sales,
#                 storage=storage,editer_commond=editer_commond,anthor=anthor,category_id=category,pics=pics,
#                      c_introduce=c_introduce,n_introduce=n_introduce)
# TBook.objects.create(book_name=book_name,dangdang_price=dangdang_price,market_price=market_price,sales=sales,
#                 storage=storage,editer_commond=editer_commond,anthor=anthor,category_id=category,pics=pics,
#                      c_introduce=c_introduce,n_introduce=n_introduce)