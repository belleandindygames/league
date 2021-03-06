from django.conf import settings
from django.conf.urls import url

from .views import get_summoner_v3, live_match, test_something, live_match_detail, FrontendAppView, ApiLiveMatch, ChampionInfoView
urlpatterns = [
    url(r'^summoner/', get_summoner_v3, name='summoner_lookup'),
    url(r'^live/$', live_match, name='live_match'),
    url(r'^live/([a-zA-Z0-9]+)/(.+)/$', live_match_detail, name='live-match-detail'),
    url(r'^api/live/([a-zA-Z0-9]+)/(.+)/$', ApiLiveMatch.as_view(), name='api-live-match'),
    url(r'api/champions/$', ChampionInfoView.as_view(), name='api-champion-info'),
    url(r'^summonerprofile/', get_summoner_v3, name='summoner_profile'),
    url(r'test/', test_something, name='test'),
    url(r'^', FrontendAppView.as_view()),
]