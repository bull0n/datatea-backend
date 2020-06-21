
from teas.models import Tea
from graphene_django.types import DjangoObjectType

import graphene

class TeaType(DjangoObjectType):
    class Meta:
        model = Tea


class Query(object):
    all_teas = graphene.List(TeaType)

    def resolve_all_teas(self, info, **kwargs):
        return Tea.objects.all()
