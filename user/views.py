from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import UserSerializer


class LoginAPIView(APIView):

    def post(self, request):
        data = request.POST
        serializer = UserSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data.get("user")
            token, object = Token.objects.get_or_create(user=user)
            return Response({"Token": token.key})


class LogoutAPIView(APIView):
    def get(self, request):
        user = request.user
        token = Token.objects.get(user=user)
        token.delete()
        return Response(status=status.HTTP_401_UNAUTHORIZED)




