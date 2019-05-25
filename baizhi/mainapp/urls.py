from django.urls import path
from mainapp import views

app_name = "mainapp"

urlpatterns = [
    path('index/',views.index,name="index"),
    path('delindex/',views.delindex,name="delindex"),
    path('index_c/',views.index_c,name="index_c"),
    path('delindex_c/',views.delindex_c,name="delindex_c"),
    path('bookdetails/',views.bookdetails,name="bookdetails"),
    path('delbookdetails/',views.delbookdetails,name="delbookdetails"),
    path('addbook/',views.addbook,name="addbook"),      #添加书籍
    path('indent/',views.indent,name="indent"),
    path('t_indent/',views.t_indent,name="t_indent"),
    path('address/',views.address,name="address"),
    path('indentok/',views.indentok,name="indentok"),
    path('login/',views.login,name="login"),
    path('register/',views.register,name="register"),
    path('registerok/',views.registerok,name="registerok"),
    path('car/',views.car,name="car"),
    path('delcar/',views.delcar,name="delcar"),
    path('updetecar/',views.updetecar,name="updetecar"),    #修改货物加减
    path('updetecar1/',views.updetecar1,name="updetecar1"),  # 修改货物中间值
]
