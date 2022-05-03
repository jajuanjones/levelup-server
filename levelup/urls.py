from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from levelupapi.views import register_user, login_user
from rest_framework import routers
from levelupapi.views import GameTypeView
from levelupapi.views import GameView
from levelupapi.views import GamerView
from levelupapi.views import EventView
from levelupapi.views import EventGamerView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'gametypes', GameTypeView, 'gametype')
router.register(r'games', GameView, 'game')
router.register(r'gamers', GamerView, 'gamer')
router.register(r'events', EventView, 'event')
router.register(r'eventgamers', EventGamerView, 'eventgamer')


urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]