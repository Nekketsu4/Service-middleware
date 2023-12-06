from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api_route.services.children import *
from api_route.serializers import RegAuthSerializer



class BotListView(APIView):
    """Информация списка ботов"""

    def get(self, request):
        bots = BotList()
        bots.send(uri='/bots', method=request.method)
        return Response(bots.get_response().json(), status=bots.get_response().status_code)


class BotDetailView(APIView):
    """Информация о боте"""

    def get(self, request, pk):
        bot = BotDetail()
        bot.send(uri='/bots/' + str(pk), method=request.method)
        return Response(bot.get_response().json(), status=bot.get_response().status_code)


class RegUserRouteView(APIView):
    """Регистрация пользователя"""


    def get(self, request):
        reg = RegUserRoute()
        reg.send(uri='/users', method=request.method)
        return Response(reg.get_response().json(), status=reg.get_response().status_code)

    def post(self, request):
        serializer = RegAuthSerializer(data=request.data)
        if serializer.is_valid():
            validated = serializer.validated_data
            reg = RegUserRoute()
            reg.set_parameters(data=validated)
            reg.send(uri='/users', method=request.method)
            return Response(reg.get_response().json(), status=reg.get_response().status_code)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthUserRouteView(APIView):
    """Авторизация пользователя"""

    def get(self, request):
        auth = AuthUserRoute()
        auth.send(uri='/users/login', method=request.method)
        return Response(auth.get_response().json(), status=auth.get_response().status_code)

    def post(self, request):
        serializer = RegAuthSerializer(data=request.data)
        if serializer.is_valid():
            validated = serializer.validated_data
            auth = AuthUserRoute()
            auth.set_parameters(data=validated)
            auth.send(uri='/users/login', method=request.method)
            return Response(auth.get_response().json(), status=auth.get_response().status_code)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



