from api_route.route.route import Route


class BotList(Route):
    """ Информация по боту """

    def send(self, uri: str, method='GET'):
        # Некая логика (например проверить статусы кода и выполнить какие либо действия)

        super().send(uri=uri, method=method)
        return self.get_response()


class BotDetail(Route):
    """ Информация по ботам """

    def send(self, uri: str, method='GET'):
        # Некая логика (например проверить статусы кода и выполнить какие либо действия)

        super().send(uri=uri, method=method)
        return self.get_response()


class RegUserRoute(Route):
    """ Регистрация пользователя """

    def send(self, uri: str, method='POST'):
        # Некая логика (например проверить статусы кода и выполнить какие либо действия)

        super().send(uri=uri, method=method)
        return self.get_response()


class AuthUserRoute(Route):
    """ Авторизация пользователя """

    def send(self, uri: str, method='POST'):
        # Некая логика (например проверить статусы кода и выполнить какие либо действия)

        super().send(uri=uri, method=method)
        return self.get_response()


# data = {
#     "email": "string@mail.ru",
#     "password": "string"
#        }


# bot = BotList()
# print(bot.send())
#
# botD = BotDetails()
# print(botD.send())

# reg = RegUserRoute()
# reg.set_parameters(data=data)
# print(reg.send())
#
# aut = AuthUserRoute()
# aut.set_parameters(data=data)
# print(aut.send())
