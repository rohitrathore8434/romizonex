from django.shortcuts import render,redirect,HttpResponse
# from ZONEHUB.models import REGISTERX,EmailForm,h_todaydeals,h_toppicks,deal_all
from ZONEHUB.models import *

from django.core.mail import send_mail
from django.conf import settings

import random



# Create your views here.
def basex(request):
    return render(request,"basex.html")

def base(request):
    return render(request,"base.html")

def home(request):
    print("this is home file")
    todayx=h_todaydeals.objects.all()
    top=h_toppicks.objects.all()
    blogy=h_blogs.objects.all()
    n=request.session.get("user_name")
    tt={"data":todayx,"pk":top,"userx":n,"blogx":blogy}
    return render(request,"home.html",tt)
    

def register_user(request):
    otpx=random.randint(111111,999999)
    print(otpx)
    if request.method=="POST":
        full_namex=request.POST.get("name")
        emailx=request.POST.get("email")
        print(emailx,otpx)
        EmailForm.objects.create(email=emailx,otp=otpx)
        print("yyyyyyyyyyyyyyyyyyyyyy")
        send_mail(
            subject="Your OTP Code is Here",
            message=f"This is your otp for login {otpx}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[emailx],
            fail_silently=False,
            )
        data_email={"em":emailx}
        print("xxx",data_email)
        savex=REGISTERX(full_name=full_namex,email=emailx)
        savex.save()
        return render(request,"VROTP.html",data_email)
    return render(request,"register.html")

def login_user(request):
    if request.method=="POST":
        emailx=request.POST.get("email")
        passwordx=request.POST.get("password")
        print(emailx,passwordx)
        try:
            user=REGISTERX.objects.get(email=emailx,password=passwordx)
            request.session["user_id"]=user.id
            nn= request.session["user_email"]=user.email
            nn= request.session["user_name"]=user.full_name
            xx={"userx":nn}
            # return render(request,"home.html",xx)
            return redirect("/home")
        except REGISTERX.DoesNotExist:
            # da={"pp":"error"}
            return render(request,"login.html")       
    return render(request,"login.html")


def logout(request):
    request.session.flush()
    return render(request,"basex.html")   


def vrotp(request):
    if request.method=="POST":
        e=request.POST.get("email")
        o=request.POST.get("otp")
        if EmailForm.objects.filter(email=e,otp=o).exists():
            dataxx={"emm":e}
            return render(request,"set_password.html",dataxx)
        else:
            return render(request,"register.html")
    return render(request,"vrotp.html")

def set_password(request):
    if request.method=="POST":
        set_pass=request.POST.get("set_password")
        em=request.POST.get("email")
        m=REGISTERX.objects.get(email=em)
        m.password=set_pass
        m.save() 
        return render(request,"home.html")
    return render(request,"set_password.html")



def toppiks(request):
    x1=d_pickup_x1.objects.all()
    px1={"px":x1}
    return render(request,"toppicks.html",px1)

# --------------------------------------BLOG--------------------------
def blog(request):
    afs=all_fitness.objects.all()
    af=all_funny.objects.all()
    an=all_news.objects.all()
    f={"fness":afs,"funny":af,"news":an}   
    print("ddddddddddddddddddddddddddddddddd") 
    return render(request,"blogs.html",f)    

def fitness(request):
    fs=b_fitness.objects.all()
    f={"fness":fs}
    return render(request,"fitness.html",f)

def funny(request):
    bf=b_funny.objects.all()
    f={"funny":bf}
    return render(request,"funny.html",f)

def news(request):
    bn=b_news.objects.all()
    f={"news":bn}
    return render(request,"news.html",f)
# ----------------------------------------------------------------

def blog_fitnex(request, id):
        fs = b_fitness.objects.get(id=id)
        f = {"fness": fs}
        return render(request,"blog_fitness.html",f)
     
def blog_funnyx(request,id):
    bf=b_funny.objects.get(id=id)
    f={"funny":bf}
    return render(request,"blog_funny.html",f)

def blog_newsx(request,id):
    bn=b_news.objects.get(id=id)
    f={"news":bn}
    return render(request,"blog_news.html",f)
# --------------------------------------------------------------------

def all_fitnex(request, id):
    fs = all_fitness.objects.get(id=id)
    f = {"fness": fs}
    return render(request,"all_fitness.html",f)


def all_funnyx(request,id):
    bf=all_funny.objects.get(id=id)
    f={"funny":bf}
    return render(request,"all_funny.html",f)

def all_newsx(request,id):
    bn=all_news.objects.get(id=id)
    f={"news":bn}
    return render(request,"all_news.html",f)



# ----------------------deal-----------------------------------
def deal(request):
    al=deal_all.objects.all()
    ax={"allx":al}
    return render(request,"deals.html",ax)

def d_electronicx(request):
    el=d_electronic.objects.all()
    ax={"allx":el}    
    return render(request,"d_electronic.html",ax) 

def d_fitnes(request):
    ft=d_fitness.objects.all()
    ax={"allx":ft}    
    return render(request,"d_fitness.html",ax)

def d_fashionx(request):
    fs=d_fashion.objects.all()
    ax={"allx":fs}    
    return render(request,"d_fashion.html",ax)

def d_mobilex(request):
    fs=d_mobile.objects.all()
    ax={"allx":fs}    
    return render(request,"deal_mobile.html",ax)

def d_beautyx(request):
    fs=d_beauty.objects.all()
    ax={"allx":fs}    
    return render(request,"deal_beauty.html",ax)

def d_foodx(request):
    fs=d_food.objects.all()
    ax={"allx":fs}    
    return render(request,"deal_food.html",ax)

def d_kitchenx(request):
    fs=d_kitchen.objects.all()
    ax={"allx":fs}    
    return render(request,"deal_home_kitchen.html",ax)

def d_toyx(request):
    fs=d_toys.objects.all()
    ax={"allx":fs}    
    return render(request,"deal_toys.html",ax)

def d_furniturex(request):
    fs=d_furniture.objects.all()
    ax={"allx":fs}    
    return render(request,"deal_furniture.html",ax)

def d_appliancex(request):
    fs=d_appliances.objects.all()
    ax={"allx":fs}    
    return render(request,"deal_appliances.html",ax)
# ===================================FILTER=====================================
from django.http import JsonResponse

def filter_all(request,p,name):
        if p==0:
            ft = list(deal_all.objects.all().values())
            return JsonResponse({"allx":ft})
        elif p == 299:
            ft = list(deal_all.objects.filter(price__lte=299).values())
            ax={"allx":ft}
            return JsonResponse(ax) 
            
        elif p == 499:
            ft = list(deal_all.objects.filter(price__gte=300, price__lte=499).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 899:
            ft = list(deal_all.objects.filter(price__gte=500, price__lte=899).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 1499:
            ft = list(deal_all.objects.filter(price__gte=900, price__lte=1499).values())
            ax={"allx":ft}
            return JsonResponse(ax)
        
        elif p == 3000:
            ft = list(deal_all.objects.filter(price__gte=1500, price__lte=3000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 5000:
            ft = list(deal_all.objects.filter(price__gte=3001, price__lte=5000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 10000:
            ft = list(deal_all.objects.filter(price__gte=5001, price__lte=10000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 20000:
            ft = list(deal_all.objects.filter(price__gte=10001, price__lte=20000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 50000:
            ft = list(deal_all.objects.filter(price__gte=20001, price__lte=50000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 100000:
            ft = list(deal_all.objects.filter(price__gte=50001, price__lte=100000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        # else:
        #     ft = deal_all.objects.all()        
        #     ax={"allx":ft}
        #     return render(request,"deals.html",ax)
        
# ---------------------------FILTER ELECTRONIC--------------------------------------
def filter_electronic(request,p,name):
        if p==0:
            ft = list(d_electronic.objects.all().values())
            return JsonResponse({"allx":ft})
        elif p == 299:
            ft = list(d_electronic.objects.filter(price__lte=299).values())
            ax={"allx":ft}
            return JsonResponse(ax) 
            
        elif p == 499:
            ft = list(d_electronic.objects.filter(price__gte=300, price__lte=499).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 899:
            ft = list(d_electronic.objects.filter(price__gte=500, price__lte=899).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 1499:
            ft = list(d_electronic.objects.filter(price__gte=900, price__lte=1499).values())
            ax={"allx":ft}
            return JsonResponse(ax)
        
        elif p == 3000:
            ft = list(d_electronic.objects.filter(price__gte=1500, price__lte=3000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 5000:
            ft = list(d_electronic.objects.filter(price__gte=3001, price__lte=5000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 10000:
            ft = list(d_electronic.objects.filter(price__gte=5001, price__lte=10000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 20000:
            ft = list(d_electronic.objects.filter(price__gte=10001, price__lte=20000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 50000:
            ft = list(d_electronic.objects.filter(price__gte=20001, price__lte=50000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 100000:
            ft = list(d_electronic.objects.filter(price__gte=50001, price__lte=100000).values())
            ax={"allx":ft}
            return JsonResponse(ax)   




# ---------------------------FILTER FITNESS--------------------------------------

def filter_fitness(request,p,name):
        if p==0:
            ft = list(d_fitness.objects.all().values())
            return JsonResponse({"allx":ft})
        elif p == 299:
            ft = list(d_fitness.objects.filter(price__lte=299).values())
            ax={"allx":ft}
            return JsonResponse(ax) 
            
        elif p == 499:
            ft = list(d_fitness.objects.filter(price__gte=300, price__lte=499).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 899:
            ft = list(d_fitness.objects.filter(price__gte=500, price__lte=899).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 1499:
            ft = list(d_fitness.objects.filter(price__gte=900, price__lte=1499).values())
            ax={"allx":ft}
            return JsonResponse(ax)
        
        elif p == 3000:
            ft = list(d_fitness.objects.filter(price__gte=1500, price__lte=3000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 5000:
            ft = list(d_fitness.objects.filter(price__gte=3001, price__lte=5000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 10000:
            ft = list(d_fitness.objects.filter(price__gte=5001, price__lte=10000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 20000:
            ft = list(d_fitness.objects.filter(price__gte=10001, price__lte=20000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 50000:
            ft = list(d_fitness.objects.filter(price__gte=20001, price__lte=50000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 100000:
            ft = list(d_fitness.objects.filter(price__gte=50001, price__lte=100000).values())
            ax={"allx":ft}
            return JsonResponse(ax)  


# ---------------------------FILTER FASHION--------------------------------------
        
def filter_fashion(request,p,name):
        if p==0:
            ft = list(d_fashion.objects.all().values())
            return JsonResponse({"allx":ft})
        elif p == 299:
            ft = list(d_fashion.objects.filter(price__lte=299).values())
            ax={"allx":ft}
            return JsonResponse(ax) 
            
        elif p == 499:
            ft = list(d_fashion.objects.filter(price__gte=300, price__lte=499).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 899:
            ft = list(d_fashion.objects.filter(price__gte=500, price__lte=899).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 1499:
            ft = list(d_fashion.objects.filter(price__gte=900, price__lte=1499).values())
            ax={"allx":ft}
            return JsonResponse(ax)
        
        elif p == 3000:
            ft = list(d_fashion.objects.filter(price__gte=1500, price__lte=3000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 5000:
            ft = list(d_fashion.objects.filter(price__gte=3001, price__lte=5000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 10000:
            ft = list(d_fashion.objects.filter(price__gte=5001, price__lte=10000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 20000:
            ft = list(d_fashion.objects.filter(price__gte=10001, price__lte=20000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 50000:
            ft = list(d_fashion.objects.filter(price__gte=20001, price__lte=50000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 100000:
            ft = list(d_fashion.objects.filter(price__gte=50001, price__lte=100000).values())
            ax={"allx":ft}
            return JsonResponse(ax)       
        


# ---------------------------FILTER MOBILES--------------------------------------

def filter_mobile(request,p,name):
        if p==0:
            ft = list(d_mobile.objects.all().values())
            return JsonResponse({"allx":ft})
        elif p == 299:
            ft = list(d_mobile.objects.filter(price__lte=299).values())
            ax={"allx":ft}
            return JsonResponse(ax) 
            
        elif p == 499:
            ft = list(d_mobile.objects.filter(price__gte=300, price__lte=499).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 899:
            ft = list(d_mobile.objects.filter(price__gte=500, price__lte=899).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 1499:
            ft = list(d_mobile.objects.filter(price__gte=900, price__lte=1499).values())
            ax={"allx":ft}
            return JsonResponse(ax)
        
        elif p == 3000:
            ft = list(d_mobile.objects.filter(price__gte=1500, price__lte=3000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 5000:
            ft = list(d_mobile.objects.filter(price__gte=3001, price__lte=5000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 10000:
            ft = list(d_mobile.objects.filter(price__gte=5001, price__lte=10000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 20000:
            ft = list(d_mobile.objects.filter(price__gte=10001, price__lte=20000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 50000:
            ft = list(d_mobile.objects.filter(price__gte=20001, price__lte=50000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 100000:
            ft = list(d_mobile.objects.filter(price__gte=50001, price__lte=100000).values())
            ax={"allx":ft}
            return JsonResponse(ax)


# ---------------------------FILTER BEAUTY--------------------------------------

def filter_beauty(request,p,name):
        if p==0:
            ft = list(d_beauty.objects.all().values())
            return JsonResponse({"allx":ft})
        elif p == 299:
            ft = list(d_beauty.objects.filter(price__lte=299).values())
            ax={"allx":ft}
            return JsonResponse(ax) 
            
        elif p == 499:
            ft = list(d_beauty.objects.filter(price__gte=300, price__lte=499).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 899:
            ft = list(d_beauty.objects.filter(price__gte=500, price__lte=899).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 1499:
            ft = list(d_beauty.objects.filter(price__gte=900, price__lte=1499).values())
            ax={"allx":ft}
            return JsonResponse(ax)
        
        elif p == 3000:
            ft = list(d_beauty.objects.filter(price__gte=1500, price__lte=3000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 5000:
            ft = list(d_beauty.objects.filter(price__gte=3001, price__lte=5000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 10000:
            ft = list(d_beauty.objects.filter(price__gte=5001, price__lte=10000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 20000:
            ft = list(d_beauty.objects.filter(price__gte=10001, price__lte=20000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 50000:
            ft = list(d_beauty.objects.filter(price__gte=20001, price__lte=50000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 100000:
            ft = list(d_beauty.objects.filter(price__gte=50001, price__lte=100000).values())
            ax={"allx":ft}
            return JsonResponse(ax)

# ---------------------------FILTER FOOD--------------------------------------

def filter_food(request,p,name):
        if p==0:
            ft = list(d_food.objects.all().values())
            return JsonResponse({"allx":ft})
        elif p == 299:
            ft = list(d_food.objects.filter(price__lte=299).values())
            ax={"allx":ft}
            return JsonResponse(ax) 
            
        elif p == 499:
            ft = list(d_food.objects.filter(price__gte=300, price__lte=499).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 899:
            ft = list(d_food.objects.filter(price__gte=500, price__lte=899).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 1499:
            ft = list(d_food.objects.filter(price__gte=900, price__lte=1499).values())
            ax={"allx":ft}
            return JsonResponse(ax)
        
        elif p == 3000:
            ft = list(d_food.objects.filter(price__gte=1500, price__lte=3000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 5000:
            ft = list(d_food.objects.filter(price__gte=3001, price__lte=5000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 10000:
            ft = list(d_food.objects.filter(price__gte=5001, price__lte=10000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 20000:
            ft = list(d_food.objects.filter(price__gte=10001, price__lte=20000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 50000:
            ft = list(d_food.objects.filter(price__gte=20001, price__lte=50000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 100000:
            ft = list(d_food.objects.filter(price__gte=50001, price__lte=100000).values())
            ax={"allx":ft}
            return JsonResponse(ax)

# ---------------------------FILTER KITCHEN--------------------------------------

def filter_kitchen(request,p,name):
        if p==0:
            ft = list(d_kitchen.objects.all().values())
            return JsonResponse({"allx":ft})
        elif p == 299:
            ft = list(d_kitchen.objects.filter(price__lte=299).values())
            ax={"allx":ft}
            return JsonResponse(ax) 
            
        elif p == 499:
            ft = list(d_kitchen.objects.filter(price__gte=300, price__lte=499).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 899:
            ft = list(d_kitchen.objects.filter(price__gte=500, price__lte=899).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 1499:
            ft = list(d_kitchen.objects.filter(price__gte=900, price__lte=1499).values())
            ax={"allx":ft}
            return JsonResponse(ax)
        
        elif p == 3000:
            ft = list(d_kitchen.objects.filter(price__gte=1500, price__lte=3000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 5000:
            ft = list(d_kitchen.objects.filter(price__gte=3001, price__lte=5000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 10000:
            ft = list(d_kitchen.objects.filter(price__gte=5001, price__lte=10000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 20000:
            ft = list(d_kitchen.objects.filter(price__gte=10001, price__lte=20000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 50000:
            ft = list(d_kitchen.objects.filter(price__gte=20001, price__lte=50000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 100000:
            ft = list(d_kitchen.objects.filter(price__gte=50001, price__lte=100000).values())
            ax={"allx":ft}
            return JsonResponse(ax)


# ---------------------------FILTER TOYS--------------------------------------

def filter_toys(request,p,name):
        if p==0:
            ft = list(d_toys.objects.all().values())
            return JsonResponse({"allx":ft})
        elif p == 299:
            ft = list(d_toys.objects.filter(price__lte=299).values())
            ax={"allx":ft}
            return JsonResponse(ax) 
            
        elif p == 499:
            ft = list(d_toys.objects.filter(price__gte=300, price__lte=499).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 899:
            ft = list(d_toys.objects.filter(price__gte=500, price__lte=899).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 1499:
            ft = list(d_toys.objects.filter(price__gte=900, price__lte=1499).values())
            ax={"allx":ft}
            return JsonResponse(ax)
        
        elif p == 3000:
            ft = list(d_toys.objects.filter(price__gte=1500, price__lte=3000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 5000:
            ft = list(d_toys.objects.filter(price__gte=3001, price__lte=5000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 10000:
            ft = list(d_toys.objects.filter(price__gte=5001, price__lte=10000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 20000:
            ft = list(d_toys.objects.filter(price__gte=10001, price__lte=20000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 50000:
            ft = list(d_toys.objects.filter(price__gte=20001, price__lte=50000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 100000:
            ft = list(d_toys.objects.filter(price__gte=50001, price__lte=100000).values())
            ax={"allx":ft}
            return JsonResponse(ax)


# ---------------------------FILTER FURNITURE--------------------------------------

def filter_furniture(request,p,name):
        if p==0:
            ft = list(d_furniture.objects.all().values())
            return JsonResponse({"allx":ft})
        elif p == 299:
            ft = list(d_furniture.objects.filter(price__lte=299).values())
            ax={"allx":ft}
            return JsonResponse(ax) 
            
        elif p == 499:
            ft = list(d_furniture.objects.filter(price__gte=300, price__lte=499).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 899:
            ft = list(d_furniture.objects.filter(price__gte=500, price__lte=899).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 1499:
            ft = list(d_furniture.objects.filter(price__gte=900, price__lte=1499).values())
            ax={"allx":ft}
            return JsonResponse(ax)
        
        elif p == 3000:
            ft = list(d_furniture.objects.filter(price__gte=1500, price__lte=3000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 5000:
            ft = list(d_furniture.objects.filter(price__gte=3001, price__lte=5000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 10000:
            ft = list(d_furniture.objects.filter(price__gte=5001, price__lte=10000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 20000:
            ft = list(d_furniture.objects.filter(price__gte=10001, price__lte=20000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 50000:
            ft = list(d_furniture.objects.filter(price__gte=20001, price__lte=50000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 100000:
            ft = list(d_furniture.objects.filter(price__gte=50001, price__lte=100000).values())
            ax={"allx":ft}
            return JsonResponse(ax)

# ---------------------------FILTER APPLIANcCES--------------------------------------

def filter_appliance(request,p,name):
        if p==0:
            ft = list(d_appliances.objects.all().values())
            return JsonResponse({"allx":ft})
        elif p == 299:
            ft = list(d_appliances.objects.filter(price__lte=299).values())
            ax={"allx":ft}
            return JsonResponse(ax) 
            
        elif p == 499:
            ft = list(d_appliances.objects.filter(price__gte=300, price__lte=499).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 899:
            ft = list(d_appliances.objects.filter(price__gte=500, price__lte=899).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 1499:
            ft = list(d_appliances.objects.filter(price__gte=900, price__lte=1499).values())
            ax={"allx":ft}
            return JsonResponse(ax)
        
        elif p == 3000:
            ft = list(d_appliances.objects.filter(price__gte=1500, price__lte=3000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 5000:
            ft = list(d_appliances.objects.filter(price__gte=3001, price__lte=5000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 10000:
            ft = list(d_appliances.objects.filter(price__gte=5001, price__lte=10000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 20000:
            ft = list(d_appliances.objects.filter(price__gte=10001, price__lte=20000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 50000:
            ft = list(d_appliances.objects.filter(price__gte=20001, price__lte=50000).values())
            ax={"allx":ft}
            return JsonResponse(ax)        

        elif p == 100000:
            ft = list(d_appliances.objects.filter(price__gte=50001, price__lte=100000).values())
            ax={"allx":ft}
            return JsonResponse(ax)

def searchx(request):
    if request.method=="POST":
        allx=request.POST.get("find")
        if allx=="":
            todayx=h_todaydeals.objects.all()
            top=h_toppicks.objects.all()
            blogy=h_blogs.objects.all()
            n=request.session.get("user_name")
            tt={"data":todayx,"pk":top,"userx":n,"blogx":blogy}
            return render(request,"home.html",tt)
            
        allx = allx.strip().lower()
        x1=deal_all.objects.filter(name__icontains=allx)
        x2=d_electronic.objects.filter(name__icontains=allx)
        x3=d_fitness.objects.filter(name__icontains=allx)
        x4=d_fashion.objects.filter(name__icontains=allx)
        x5=d_mobile.objects.filter(name__icontains=allx)
        x6=d_beauty.objects.filter(name__icontains=allx)
        x7=d_food.objects.filter(name__icontains=allx)
        x8=d_kitchen.objects.filter(name__icontains=allx)
        x9=d_toys.objects.filter(name__icontains=allx)
        x10=d_furniture.objects.filter(name__icontains=allx)
        x11=d_appliances.objects.filter(name__icontains=allx)


        x12=b_fitness.objects.filter(title__icontains=allx)
        x13=b_funny.objects.filter(title__icontains=allx)
        x14=b_news.objects.filter(title__icontains=allx)


       
       
        
        all_data = list(x1) + list(x2) + list(x3) + list(x4) + list(x5) + list(x6) + list(x7) + list(x8) + list(x9) + list(x10) + list(x11)

        all_data2=list(x12)
        all_data3=list(x13)
        all_data4=list(x14)

        y={
            "yy":all_data,
            "fness":all_data2,
            "funny":all_data3,
            "news":all_data4,
            "user_data":allx,
            }
     
        return render(request,"search.html",y)
    return render(request,"search.html")
        

def privacy(request):
    return render(request,"privacy.html")

def disclaimer(request):
    return render(request,"disclaimer.html")

def term_condition(request):
    return render(request,"terms_condition.html")
def contect_us(request):
    return render(request,"contect_us.html")

def home_fitness(request, cetegory):
    if cetegory == "fitness":
        fs=b_fitness.objects.all()
        f={"fness":fs}
        return render(request, "fitness.html",f)
    elif cetegory=="funny":
        bf=b_funny.objects.all()
        f={"funny":bf}
        return render(request,"funny.html",f)
    elif cetegory=="news":
        bn=b_news.objects.all()
        f={"news":bn}
        return render(request,"news.html",f)
    elif cetegory=="fitness product":
        ft=d_fitness.objects.all()
        ax={"allx":ft}  
        return render(request,"d_fitness.html",ax)