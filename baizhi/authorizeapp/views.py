from datetime import datetime
from django.contrib.auth.hashers import make_password,check_password
from django.shortcuts import render,HttpResponse,redirect
from captcha.image import ImageCaptcha
from django.core.mail import EmailMultiAlternatives
from mainapp.models import TBook,TCategory,TUser,TOrderitem,TOrder,TAddress,Confirm_string
# Create your views here.
import random,string,re,hashlib

def login(request):
    indent = request.COOKIES.get("indent")
    email = request.COOKIES.get("email")
    pwd = request.COOKIES.get("pwd")
    # username = request.COOKIES.get("username")
    user = TUser.objects.filter(email=email)
    if user:
        if user[0].status == 1:
            c_pwd = user[0].password
            # print(check_password(pwd,c_pwd),17)
            if check_password(pwd,c_pwd):
                request.session["login"] = "ok"
                if indent:
                    return redirect("mainapp:indent")
                return redirect("mainapp:index")
            return render(request, 'baizhi/login.html')
        return HttpResponse("账户未激活，请在自己的邮箱激活")
    else:
        return render(request, 'baizhi/login.html')



def loginlogic(request):
    indent = request.COOKIES.get("indent")
    email = request.POST.get("txtusername")
    pwd = request.POST.get("txtpassword")
    save = request.POST.get("autologin")
    code1 = request.POST.get("code1")  #从网页获得
    code2 = request.session.get('code')  # 从session里获得
    user = TUser.objects.filter(email=email)
    if user:                          #判断数据库有没有这个数据
        c_pwd = user[0].password
        if check_password(pwd,c_pwd) and code1.upper() == code2.upper():   #判断密码跟验证码是否争取
            if user[0].status == 1:
                red_index = redirect("mainapp:index")
                red = redirect("mainapp:indent")
                red.set_cookie("email",email)
                red.set_cookie('username', user[0].username)
                if save:                        #判断是否保存账号密码
                    if indent:
                        red.set_cookie('email', email, max_age=60 * 60 * 24)
                        red.set_cookie("username",user[0].username,max_age=60 * 60 * 24)
                        return red
                    red_index.set_cookie('email', email, max_age=60 * 60 * 24)
                    red_index.set_cookie('username', user[0].username, max_age=60 * 60 * 24)
                    return red_index
                else:
                    if indent:
                        red.set_cookie('email', email)
                        red.set_cookie("username", user[0].username)
                        return red
                    red_index.set_cookie('email', email)
                    red_index.set_cookie('username',user[0].username)
                    return red_index
            return HttpResponse("账户未激活，请在自己的邮箱激活")
        else:
            return HttpResponse("用户名或者密码错误")
    return HttpResponse("用户名或者密码错误")


def register(request):
    return render(request,"baizhi/register.html")


def hash_cide(email,now):
    h = hashlib.md5()
    email += now
    h.update(email.encode())
    return h.hexdigest()


def make_confirm_string(new_user):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    code = hash_cide(new_user.email,now)
    Confirm_string.objects.create(code=code,user_id=new_user.id,email=new_user.email)
    return code


def registerlogic(request):
    p_email = request.POST.get("txt_username")
    username = request.POST.get("checkuser1")
    pwd1 = request.POST.get("pwd1")
    pwd2 = request.POST.get("pwd2")
    code1 = request.POST.get("code1")       #从网页获得
    code2 = request.session.get('code')   #从session里获得
    c_email = re.findall('^1[0-9]{10}$|^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$',p_email)
    if c_email:
        ok_email = TUser.objects.filter(email=p_email)
        if not ok_email:
            c_pwd = re.findall("^\w{6,20}$",pwd1)
            if c_pwd:
                c_username = re.findall("^\w{3,20}$", username)
                if c_username and pwd1 == pwd2 and code1.upper() == code2.upper():
                    pwd1 = make_password(pwd1)
                    new_user = TUser.objects.create(email=p_email,password=pwd1,username=username)
                    red1 = redirect("authorizeapp:registerok")
                    red1.set_cookie("email",p_email)
                    red1.set_cookie('username', username)
                    red1.set_cookie('pwd', pwd2)
                    request.session["regist"] = "ok"
                    code = make_confirm_string(new_user)
                    post_email(p_email,code)
                    return red1
    return HttpResponse("注册失败")



def post_email(email,code):
    subject, from_email, to = '来自的注册激活邮件', 'zouyi1984@sina.cn', '{}'.format(email)
    text_content = '欢迎访问www.baidu.com，祝贺你收到了我的邮件，有幸收到我的邮件说明你及其幸运'
    html_content = '<p>感谢注册<a href="http://{}/authorize/verify_emil/?code={}"target=blank>点击这里激活</a>，\欢迎你来验证你的邮箱，验证结束你就可以登录了！</p>'.format("127.0.0.1:8000",code)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def verify_emil(request):  #验证邮箱
    code = request.GET.get("code")
    email_ok = Confirm_string.objects.filter(code=code)
    if email_ok:
        user = TUser.objects.get(confirm_string__code=code)
        user.status = 1
        user.save()
        email_ok.delete()
        return redirect("authorizeapp:login")
    return HttpResponse("激活失败")


def registerok(request):
    regist = request.session.get("regist")
    if regist:
        p_email = request.COOKIES.get("email")
        return render(request,"baizhi/register ok.html",{"p_email":p_email})
    return redirect("authorizeapp:login")


def getcapcha(request):                #验证码
    image = ImageCaptcha()
    #随机生成5位数的大小写字母或数字的验证码
    rand_code = random.sample(string.ascii_letters+string.digits,3)
    rand_code = "".join(rand_code)          #转换成字符串
    data = image.generate(rand_code)        #验证码放在图片里
    request.session["code"] = rand_code     #吧验证码上传到session数据库中
    return HttpResponse(data,"image/png")


def checkemail(request):
    c_email = request.GET.get("c_email")
    z = re.findall('^1[0-9]{10}$|^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$',c_email)
    if z:
        result = TUser.objects.filter(email=c_email)
        if result:
            return HttpResponse("1")
        else:
            return HttpResponse("2")
    else:
        return HttpResponse('3')


def checkcode(request):
    c_code = request.GET.get("checkcode")
    code = request.session.get('code')
    if c_code.upper() == code.upper():
        return HttpResponse("1")
    else:
        return HttpResponse("2")


# def delcode(request):
#     a = redirect("authorizeapp:register")
#     request.COOKIES.get("email").delete()
#     request.COOKIES.get("pwd").delete()
#     request.COOKIES.get("username").delete()
#     a.delete_cookie()


