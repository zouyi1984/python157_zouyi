from django.urls import path
from authorizeapp import views
app_name = "authorizeapp"

urlpatterns = [
    path('login/',views.login,name="login"),
    path('loginlogic/',views.loginlogic,name="loginlogic"),
    path('register/',views.register,name="register"),
    path('registerok/',views.registerok,name="registerok"),
    path('registerlogic/',views.registerlogic,name="registerlogic"),
    path('getcapcha/',views.getcapcha,name="getcapcha"),
    path('checkemail/',views.checkemail,name="checkemail"),
    path('checkcode/',views.checkcode,name="checkcode"),
    path('verify_emil/',views.verify_emil,name="verify_emil"),
]
