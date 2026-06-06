from django.contrib import admin

# Register your models here.
# from ZONEHUB.models import REGISTERX,EmailForm,h_todaydeals,h_toppicks,deal_all,d_electronic,d_fitness,d_fashion,deal_299,deal_499,deal_899,deal_1499,deal_3000,deal_5000,deal_10000,deal_20000,deal_50000,deal_100000
from ZONEHUB.models import *
admin.site.register(REGISTERX)
admin.site.register(EmailForm)
admin.site.register(h_todaydeals)
admin.site.register(h_toppicks)
admin.site.register(h_blogs)

admin.site.register(deal_all)
admin.site.register(d_electronic)
admin.site.register(d_fitness)
admin.site.register(d_fashion)
admin.site.register(d_mobile)
admin.site.register(d_beauty)
admin.site.register(d_food)
admin.site.register(d_kitchen)
admin.site.register(d_toys)
admin.site.register(d_furniture)
admin.site.register(d_appliances)

admin.site.register(all_fitness)
admin.site.register(all_funny)
admin.site.register(all_news)
admin.site.register(b_fitness)
admin.site.register(b_funny)
admin.site.register(b_news)

admin.site.register(d_pickup_x1)