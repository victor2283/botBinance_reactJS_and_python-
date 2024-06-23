from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import get_bot_data, index

router = DefaultRouter()
#router.register(r'items', ItemViewSet)

urlpatterns = [
    path('data/', get_bot_data, name='get_bot_data'),
    path('', index, name='index'),

]

