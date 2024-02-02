from django.urls import path
from .views import login_view
from .views import index

urlpatterns = [
    # path('', login_view, name='login'),
    path('', index, name='home'),
]






