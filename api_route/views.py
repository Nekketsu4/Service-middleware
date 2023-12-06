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
        bots.send(uri='/bots')
        return Response(bots.get_response().json(), status=bots.get_response().status_code)


class BotDetailView(APIView):
    """Информация о боте"""

    def get(self, request, pk):
        bot = BotDetail()
        bot.send(uri='/bots/' + str(pk))
        return Response(bot.get_response().json(), status=bot.get_response().status_code)


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
            reg.send(uri='/users')
            return Response(reg.get_response().json(), status=reg.get_response().status_code)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthUserRouteView(APIView):
    """Авторизация пользователя"""

    def get(self, request):
        return Response(error, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = RegAuthSerializer(data=request.data)
        if serializer.is_valid():
            validated = serializer.validated_data
            auth = AuthUserRoute()
            auth.set_parameters(data=validated)
            auth.send(uri='/users/login')
            return Response(auth.get_response().json(), status=auth.get_response().status_code)
        return Response(serializer.errors, status=request.status_code)



