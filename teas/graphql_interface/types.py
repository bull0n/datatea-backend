import graphene
from graphene_django.types import DjangoObjectType

from teas.models import Tea

class TeaType(DjangoObjectType):
    class Meta:
        model = Tea


