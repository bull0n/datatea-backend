from django.conf.urls import url, include
from django.contrib import admin

from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

urlpatterns = [
    url('', csrf_exempt(GraphQLView.as_view(graphiql=settings.DEBUG))),
]