from django.urls import path
from ZONEHUB import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path("",views.home,name="home"),
     path("basex",views.basex,name="basex"),
    path("home/",views.home,name="home"),
    path("base",views.base,name="base"),
    
    path("toppicks",views.toppiks,name="toppicks"),

    path("blogs",views.blog,name="blogs"),
    path("fitness",views.fitness,name="fitness"),
    path("funny",views.funny,name="funny"),
    path("news",views.news,name="news"),
    
    path("all_fitness/<int:id>/",views.all_fitnex,name="all_fitness"),
    path("all_funny/<int:id>/",views.all_funnyx,name="all_funny"),
    path("all_news/<int:id>/",views.all_newsx,name="all_news"),


    path("blog_fitness/<int:id>/",views.blog_fitnex,name="blog_fitness"),
    path("blog_funny/<int:id>/",views.blog_funnyx,name="blog_funny"),
    path("blog_news/<int:id>/",views.blog_newsx,name="blog_news"),

  path("home_fitness/<str:cetegory>/", views.home_fitness, name="home_fitness"),
    # path("blog_news",views.blog_news,name="blog_news"),

  

    path("register_user",views.register_user,name="register_user"),
    path("login_user",views.login_user,name="login_user"),
    path("logout_user",views.logout,name="logout"),
    path("vrotp",views.vrotp,name="vrotp"),
    path("set_password",views.set_password,name="set_password"),

    path("deals",views.deal,name="deals"),
    path("d_electronic",views.d_electronicx,name="d_electronic"),
    path("d_fitness",views.d_fitnes,name="d_fitness"),
    path("d_fashion",views.d_fashionx,name="d_fashion"),
    path("d_mobile",views.d_mobilex,name="d_mobile"),
    path("d_beauty",views.d_beautyx,name="d_beauty"),
    path("d_food",views.d_foodx,name="d_food"),
    path("d_kitchen",views.d_kitchenx,name="d_kitchen"),
    path("d_toys",views.d_toyx,name="d_toys"),
    path("d_furniture",views.d_furniturex,name="d_furniture"),
    path("d_appliances",views.d_appliancex,name="d_appliances"),

path("filter_all/<int:p>/<str:name>/",views.filter_all,name="filter_all"),
path("filter_electronic/<int:p>/<str:name>/",views.filter_electronic,name="filter_electronic"),
path("filter_fitness/<int:p>/<str:name>/",views.filter_fitness,name="filter_fitness"),
path("filter_fashion/<int:p>/<str:name>/",views.filter_fashion,name="filter_fashion"),
path("filter_mobile/<int:p>/<str:name>/",views.filter_mobile,name="filter_mobile"),
path("filter_beauty/<int:p>/<str:name>/",views.filter_beauty,name="filter_beauty"),
path("filter_food/<int:p>/<str:name>/",views.filter_food,name="filter_food"),
path("filter_kitchen/<int:p>/<str:name>/",views.filter_kitchen,name="filter_kitchen"),
path("filter_toys/<int:p>/<str:name>/",views.filter_toys,name="filter_toys"),
path("filter_furniture/<int:p>/<str:name>/",views.filter_furniture,name="filter_furniture"),
path("filter_appliance/<int:p>/<str:name>/",views.filter_appliance,name="filter_appliance"),

  path("search",views.searchx,name="search"),

  path("privacy",views.privacy,name="privacy"),
  path("disclaimer",views.disclaimer,name="disclaimer"),
  path("term_condition",views.term_condition,name="term_condition"),
  path("contect_us",views.contect_us,name="contect_us")
  
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)