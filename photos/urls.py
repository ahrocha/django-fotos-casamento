from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import PhotoViewset
from . import views

#urlpatterns = [
#    path('', views.index, name='index'),
#    path('accounts', views.PhotoViewset, name='accounts'),
#]

router = SimpleRouter()
router.register('accounts', PhotoViewset)
urlpatterns = router.urls