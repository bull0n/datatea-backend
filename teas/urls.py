from django.conf.urls import url, include
from django.contrib import admin

from graphene_django.views import GraphQLView

urlpatterns = [
    url(r'^teas$', GraphQLView.as_view(graphiql=True)),
]