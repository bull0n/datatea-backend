from django.conf.urls import url, include
from django.contrib import admin

# Create your views here.
from graphene_django.views import GraphQLView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^teas$', GraphQLView.as_view(graphiql=True)),
]
