# notification_app/urls
from django.urls import path
from .views import RegisterUser, LoginUser, SendNotification, GetNotifications

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('send_notification/', SendNotification.as_view(), name='send_notification'),
    path('notifications/', GetNotifications.as_view(), name='get_notifications'),
    # path('delete/', DeleteAllData.as_view(), name='delete'),
    
]
