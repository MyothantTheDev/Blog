from django.urls import path, include
from .views import AddFollowerView

urlpatterns = [
    path('follow/', AddFollowerView.as_view(), name="user.addfollower"),
]