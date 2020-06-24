
from teas.models import Tea
from graphene_django.types import DjangoObjectType

import graphene

class TeaType(DjangoObjectType):
    class Meta:
        model = Tea

TeaFormEnum = graphene.Enum.from_enum(Tea.Form)

class CreateTea(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        form = graphene.Argument(TeaFormEnum, required=True)
        description = graphene.String(required=True)
        would_buy_again = graphene.Boolean()
        price = graphene.Float()
        picking_season = graphene.Date()
        origin = graphene.String()
        vendor = graphene.String()
        url_bought = graphene.String()
        vendor_description = graphene.String()

    tea = graphene.Field(TeaType)

    def mutate(self, info, **kwargs):
        print(kwargs)
        tea = Tea.objects.create(**kwargs)

        return CreateTea(tea=tea)


class Mutation(object): 
    create_tea = CreateTea.Field()
    pass



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


