from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api_route.services.children import *
from api_route.serializers import RegAuthSerializer



error = {
    'error': {
        'status': '404',
        'code': 'Not Found',
        'message': 'route not found'
    }
}

class BotListView(APIView):
    """Информация списка ботов"""

    def get(self, request):
        bots = BotList()
        data = bots.send(uri='/bots')
        return Response(data=data, status=status.HTTP_200_OK)


class BotDetailView(APIView):
    """Информация о боте"""

    def get(self, request, pk):
        bot = BotDetail()
        data = bot.send(uri='/bots/' + str(pk))
        return Response(data, status=status.HTTP_200_OK)


class RegUserRouteView(APIView):
    """Регистрация пользователя"""

    def get(self, request):
        return Response(error, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = RegAuthSerializer(data=request.data)
        if serializer.is_valid():
            validated = serializer.validated_data
            reg = RegUserRoute()
            reg.set_parameters(data=validated)
            data = reg.send(uri='/users')
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthUserRouteView(APIView):
    """Авторизация пользователя"""

    def get(self, request):
        return Response(error, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = RegAuthSerializer(data=request.data)
        if serializer.is_valid():
            validated = serializer.validated_data
            reg = AuthUserRoute()
            reg.set_parameters(data=validated)
            data = reg.send(uri='/users/login')
            return Response(data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



