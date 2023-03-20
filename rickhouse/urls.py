from django.conf.urls import include
from rest_framework import routers
from rickhouseapi.views import WhiskeyView, WhiskeyDistilleryView, DistilleryView, TypeView 
from django.contrib import admin
from django.urls import path
from rickhouseapi.views import register_user, check_user

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'whiskey', WhiskeyView, 'whiskey')
router.register(r'whiskeydistillery', WhiskeyDistilleryView, 'whiskeydistillery')
router.register(r'distilleries', DistilleryView, 'distillery')
router.register(r'whiskey_types', TypeView, 'whiskey_type')

urlpatterns = [
    path('register', register_user),
    path('checkuser', check_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
