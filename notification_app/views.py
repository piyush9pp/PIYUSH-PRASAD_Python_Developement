# notification_app/views
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .models import Notification
from .serializers import UserRegisterSerializer, NotificationSerializer
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='notifications.log')

class RegisterUser(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User registered successfully", "user_id": user.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginUser(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                refresh = RefreshToken.for_user(user)
                return Response({
                    "access_token": str(refresh.access_token),
                    "token_type": "bearer"
                }, status=status.HTTP_200_OK)
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class SendNotification(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        # print(data)
        user_ids = data.get('user_ids', [])
        notifications = []
        for user_id in user_ids:
            try:
                user = User.objects.get(id=user_id)
                notification = Notification.objects.create(
                    title=data['title'],
                    message=data['message'],
                    user=user,
                    notification_type=data['notification_type']
                )
                notifications.append(notification)
                print("notification",notification)
                logging.info(f"Notification sent to user {user.username} (ID: {user_id}): {data['title']}")
            except User.DoesNotExist:
                logging.warning(f"User with ID {user_id} not found. Notification not sent.")
        # print(notifications)
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class GetNotifications(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = Notification.objects.filter(user=request.user)
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


