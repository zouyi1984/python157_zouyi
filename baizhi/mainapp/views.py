from django.core.paginator import Paginator
from django.shortcuts import render,HttpResponse,redirect
from mainapp.models import TCategory,TBook,TAddress,TOrder,TOrderitem,TUser
from mainapp import cart
import datetime,hashlib
from django.http import JsonResponse
# Create your views here.

def index(request):
    username = request.COOKIES.get("username")
    one_class = TCategory.objects.filter(pk__lt=10)
    two_class = TCategory.objects.filter(pk__gt=9)
    book = TBook.objects.all()[0:8]
    book_s = TBook.objects.all().order_by("-sales")[:6]
    new_book = TBook.objects.filter(pushish_time__gt='2019-05-14').order_by("-sales")[:5]
    return render(request,"baizhi/index.html",{"one_class":one_class,"two_class":two_class,
                "book":book,"new_book":new_book,"book_s":book_s,"username":username})


def delindex(request):
    red1 = redirect("mainapp:index")
    red1.delete_cookie("email")
    red1.delete_cookie("pwd")
    red1.delete_cookie("username")
    return red1


def index_c(request):
    username = request.COOKIES.get("username")
    o_class = request.GET.get("o_class")
    t_class = request.GET.get("t_class")
    num = request.GET.get("num")
    if not num or num.isdigit() == False:
        num = 1
    one_class = TCategory.objects.filter(pk__lt=10)
    two_class = TCategory.objects.filter(pk__gt=9)
    if t_class:
        classbook1 = TCategory.objects.get(pk=int(o_class))
        classbook2 = TCategory.objects.get(pk=int(t_class))
        c_book = TBook.objects.filter(category_id=int(t_class))
        pagtor = Paginator(c_book, per_page=4)
        total = pagtor.num_pages
        if int(num) > total:
            num = 1
        bookpage = pagtor.page(num)
        return render(request,"baizhi/booklist.html",{"c_book":bookpage,"one_class":one_class,"two_class":two_class
                ,"num":num,"o_class":o_class,"t_class":t_class,"total":total,"classbook1":classbook1,"classbook2":classbook2,
                "username":username})
    else:
        classbook1 = TCategory.objects.get(pk=o_class)
        t_class1 = TCategory.objects.filter(parent_id=o_class)
        t_id = []
        for i in t_class1:
            t_id.append(i.id)
        c_book = TBook.objects.filter(category_id__in=t_id)
        pagtor = Paginator(c_book, per_page=4)
        total = pagtor.num_pages
        if int(num) > total:
            num = 1
        bookpage = pagtor.page(num)
        return render(request,"baizhi/booklist.html",{"c_book":bookpage,"one_class":one_class,"two_class":two_class
                ,"num":num,"o_class":o_class,"total":total,"classbook1":classbook1,"username":username})


def delindex_c(request):
    red1 = redirect("mainapp:index_c")
    red1.delete_cookie("email")
    red1.delete_cookie("pwd")
    red1.delete_cookie("username")
    return red1

# def booklist(request):
#     def mydefault(u):
#         if isinstance(u, TBook):
#             return {"id": u.id, "pics": u.pics, "book_name": u.book_name, "dangdang_price": u.dangdang_price, "market_price": u.market_price,
#                     "n_introduce": u.n_introduce, "c_introduce": u.c_introduce,"anthor":u.anthor,"sales":str(u.sales)}
#     o_class = request.GET.get("o_class")
#     t_class = request.GET.get("t_class")
#     num = request.GET.get("num")
#     if not num:
#         num = 1
#     if t_class:
#         c_book = TBook.objects.filter(category_id=int(t_class))
#         pagtor = Paginator(c_book, per_page=4)
#         total = pagtor.num_pages
#         bookpage = pagtor.page(num)
#         return JsonResponse(list(users), safe=False, json_dumps_params={"default": mydefault})
#     else:
#         t_class1 = TCategory.objects.filter(parent_id=o_class)
#         t_id = []
#         for i in t_class1:
#             t_id.append(i.id)
#         c_book = TBook.objects.filter(category_id__in=t_id)
#         pagtor = Paginator(c_book, per_page=4)
#         total = pagtor.num_pages
#         bookpage = pagtor.page(num)
#     # users = TBook.objects.filter(name__icontains=cha)
#     return JsonResponse(list(users), safe=False, json_dumps_params={"default": mydefault})


def bookdetails(request):
    username = request.COOKIES.get("username")
    TBook.objects.filter()
    book_id = request.GET.get("book_id")
    book_d = TBook.objects.get(pk=int(book_id))
    c_id = book_d.category_id
    book_c2 = TCategory.objects.get(pk=int(c_id))
    book_c1 = TCategory.objects.get(pk=int(book_c2.parent_id))
    return render(request,'baizhi/Book details.html',{"book_d":book_d,"book_c1":book_c1,"book_c2":book_c2,
            "username":username})


def delbookdetails(request):
    red1 = redirect("mainapp:delbookdetails")
    red1.delete_cookie("email")
    red1.delete_cookie("pwd")
    red1.delete_cookie("username")
    return red1


"""
生成类以后在做
"""
# def t_booklist(booklist):
#     total_price = 0
#     save_price = 0
#     for i in booklist:
#         total_price += float(i["dangdang_price"]) * int(i["count"])
#         save_price += (float(i["market_price"]) - float(i["dangdang_price"])) * int(i["count"])
#         i["order_price"] = (i["dangdang_price"]) * int(i["count"])
#     return booklist



def indent(request):
    username = request.COOKIES.get("username")
    if username:
        booklist = request.session.get("booklist")
        if booklist:
            email = request.COOKIES.get("email")
            user = TUser.objects.get(email=email)
            address = TAddress.objects.filter(user_id=user.id)
            total_price = 0
            save_price = 0
            order_num = 0
            for i in booklist:
                order_num += 1
                total_price += float(i["dangdang_price"])*int(i["count"])
                save_price += (float(i["market_price"]) - float(i["dangdang_price"])) * int(i["count"])
                i["order_price"] = float(i["dangdang_price"])*int(i["count"])
                # TOrder.objects.create(user_id=user.id,book_name=i["book_name"],order_price=i["order_price"],book_id=i["id"],count=i["count"],)
            request.session["order_num"] = order_num
            request.session["total_price"] = total_price
            return render(request,'baizhi/indent.html',{"address":address,"booklist":booklist,"total_price":total_price,"save_price":save_price
                                                        ,"username":username})
        return redirect("mainapp:index")
    red1 = redirect("authorizeapp:login")
    red1.set_cookie("indent","ok")
    return red1


def address(request):
    def mydefault(u):
        if isinstance(u,TAddress):
            return {"id":u.id,"user_id":u.user_id,"zip_code":u.zip_code,"recever":u.recever,
                    "receve_address":u.receve_address,"phone":u.phone}
    address = request.GET.get("address")
    address1 = TAddress.objects.filter(pk=address)
    return JsonResponse(list(address1),safe=False,json_dumps_params={"default":mydefault})


def t_indent(request):
    email = request.COOKIES.get("email")
    if email:                   #如果登录状态则填写地址，没有则跳登录页面
        booklist = request.session.get("booklist")
        recever = request.POST.get("recever")
        r_address = request.POST.get("r_address")
        zip_code = request.POST.get("zip_code")
        phone = request.POST.get("phone")
        address1 = TAddress.objects.filter(receve_address=r_address)
        user_id = TUser.objects.get(email=email)
        if address1:               #如果有这个地址则直接跳过，没有这个地址则提交
            request.session["address"] = r_address
            request.session["recever"] = recever
            for i in booklist:      #把确认的迪昂但提交到订单列表中
                i["order_price"] = float(i["dangdang_price"]) * int(i["count"])
                TOrder.objects.create(user_id=user_id.id, book_name=i["book_name"], order_price=i["order_price"],
                                      book_id=i["id"], count=i["count"], receive_address=r_address)
            return redirect("mainapp:indentok")
        #有这个地址就只提交商品订单，没这个个地址吧商品和订单都提交
        TAddress.objects.create(recever=recever,receve_address=r_address,zip_code=zip_code,phone=phone,user_id=user_id.id)
        for i in booklist:    #把确认的订单但提交到订单列表中
            i["order_price"] = float(i["dangdang_price"]) * int(i["count"])
            TOrder.objects.create(user_id=user_id.id,book_name=i["book_name"],order_price=i["order_price"],book_id=i["id"]
                                  ,count=i["count"],receive_address=r_address)
        return redirect("mainapp:indentok")
    return redirect("authorizeapp:login")


def indentok(request):
    username = request.COOKIES.get("username")
    email = request.COOKIES.get("email")
    if email:
        del request.session["booklist"]
        address = request.session.get("address")
        recever = request.session.get("recever")
        total_price = request.session.get("total_price")
        order_num = request.session.get("order_num")
        return render(request,'baizhi/indent ok.html',{"username":username,"address":address,"recever":recever,"total_price":total_price,"order_num":order_num,})
    return redirect("mainapp:index")



def login(request):
    return render(request,'baizhi/login.html')


def register(request):
    return render(request,'baizhi/register.html')


def registerok(request):
    return render(request,'baizhi/register ok.html')


def addbook(request):   #加入购物车按钮
    booklist = []
    bookid1 = request.GET.get("bookid")
    count = int(request.GET.get("count"))
    book = TBook.objects.get(pk=int(bookid1))
    booklist1  = request.session.get("booklist")
    if booklist1:
        for i in booklist1:
            booklist.append(i)
            if  i["book_name"] == book.book_name:
                i["count"] = count + i["count"]
                request.session["booklist"] = booklist
                return HttpResponse("ok")
        booklist.append({"id":book.id,"pics":book.pics,"count":count,"book_name":book.book_name,"market_price":book.market_price,"dangdang_price":book.dangdang_price})
        request.session["booklist"] = booklist
        return HttpResponse("ok")
    booklist.append({"id":book.id,"count":count,"pics":book.pics,"book_name":book.book_name,"market_price":book.market_price,"dangdang_price":book.dangdang_price})
    request.session["booklist"] = booklist
    return HttpResponse("ok")


def car(request):
    username = request.COOKIES.get("username")
    booklist = request.session.get("booklist")
    save_price = 0
    total_price = 0
    if booklist:
        for i in booklist:
            total_price += float(i["dangdang_price"]) * int(i["count"])
            save_price += (float(i["market_price"]) - float(i["dangdang_price"])) * int(i["count"])
        return render(request, 'baizhi/car.html',{"booklist":booklist,"total_price":total_price,"save_price":save_price,"username":username})
    return render(request,'baizhi/car.html',{"username":username})


def updetecar(request):
    bookid = request.GET.get("bookid")
    count = request.GET.get("id_num")
    booklist = request.session.get("booklist")
    for i in booklist:
        if i["id"] == bookid:
            count1 = i["count"]
            i["count"] = count
    request.session["booklist"] = booklist
    return HttpResponse(str(count1))


def updetecar1(request):
    bookid = request.GET.get("bookid")
    judge = request.GET.get("id_num")
    booklist = request.session.get("booklist")
    for i in booklist:
        if i["id"] == bookid:
            if judge:
                i["count"] = 1 + int(i["count"])
            else:
                i["count"] = int(i["count"]) - 1
    request.session["booklist"] = booklist
    return HttpResponse("ok")


def delcar(request):
    bookid = request.GET.get("bookid")
    booklist = request.session.get("booklist")
    for i in booklist:
        if int(bookid) == i["id"]:
            booklist.remove(i)
    request.session["booklist"] = booklist
    return redirect("mainapp:car")


# class Cartltem():
#     def __init__(self,book,amount):
#         self.amount = amount
#         self.book = book
#         # self.status = 1
#
#
# class Cart():
#     def __init__(self):
#         self.save_price = 0
#         self.total_price = 0
#         self.cartltem = []
#         #计算购物车中上面的节省金额和总金额
#
#
#     def sums(self):
#         self.total_price = 0
#         self.save_price = 0
#         for i in self.cartltem:
#             self.total_price += i.book.dangdang_price * i.amount
#             self.save_price += (i.book.market_price - i.book.dangdang_price)*i.amount
#
#
#         #向购物车中添加书籍
#     def add_book_toCart(self,book):
#         for i in self.cartltem:
#             if i.book.id == book.id:
#                 i.amount += 1
#                 self.sums()
#                 return None
#         self.cartltem.append(Cartltem(book,1))
#         self.sums()
#
#         #修改购物成的商品信息
#     def modify_cait(self,book,amount):
#         for i in self.cartltem:
#             if i.book.id == book.id:
#                 i.amount = amount
#         self.sums()
#         #删除购物车
#     def delete_book(self,book):
#         for i in self.cartltem:
#             if i.book.id == book.id:
#                 self.cartltem.remove(i)
#         self.sums()
