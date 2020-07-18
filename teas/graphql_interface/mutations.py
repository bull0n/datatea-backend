import graphene

from .types import TeaType, TeaFormEnum
from teas.models import Tea

class CreateTea(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
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