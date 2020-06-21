
from teas.models import Tea
from graphene_django.types import DjangoObjectType

import graphene

class TeaType(DjangoObjectType):
    class Meta:
        model = Tea


class Query(object):
    all_teas = graphene.List(TeaType)

    tea = graphene.Field(TeaType,
                        id=graphene.Int(),
                        name=graphene.String())


    def resolve_all_teas(self, info, **kwargs):
        return Tea.objects.all()

    def resolve_category(self, info, **kwargs):
          id = kwargs.get('id')
          name = kwargs.get('name')

          if id is not None:
              return Tea.objects.get(pk=id)

          if name is not None:
              return Tea.objects.get(name=name)

          return None


