from proxy import Route


class BotList(Route):

    def send(self):
        # Некая логика (например проверить статусы кода и выполнить какие либо действия)

        super().send(uri='/bots')
        return self.get_response()


class BotDetails(Route):

    def send(self):
        # Некая логика (например проверить статусы кода и выполнить какие либо действия)

        super().send('/bots/2')
        return self.get_response()


class RegUserRoute(Route):

    def send(self):
        # Некая логика (например проверить статусы кода и выполнить какие либо действия)

        super().send(uri='/users', method='POST')
        return self.get_response()


class AuthUserRoute(Route):

    def send(self):
        # Некая логика (например проверить статусы кода и выполнить какие либо действия)

        super().send(uri='/users/login', method='POST')
        return self.get_response()


data = {
    'email': 'string@mail.ru',
    'password': 'string'
       }


bot = BotList()
print(bot.send())

botD = BotDetails()
print(botD.send())

reg = RegUserRoute()
reg.set_parameters(data=data)
print(reg.send())

aut = AuthUserRoute()
aut.set_parameters(data=data)
print(aut.send())
