from django.urls import path

from api_route.views import BotListView, BotDetailView, RegUserRouteView, AuthUserRouteView

urlpatterns = [
    path('bots/', BotListView.as_view()),
    path('bots/<int:pk>/', BotDetailView.as_view()),
    path('reg/', RegUserRouteView.as_view()),
    path('auth/', AuthUserRouteView.as_view()),
]