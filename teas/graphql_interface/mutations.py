import graphene

from .types import TeaType
from teas.models import Tea
from users.decorators import auth_required

class CreateTea(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
        name = graphene.String(required=True)
        comment = graphene.String()
        would_buy_again = graphene.Boolean()
        price = graphene.Float()
        picking_season = graphene.Date()
        origin = graphene.String()
        vendor = graphene.String()
        url_bought = graphene.String()
        vendor_description = graphene.String()

    tea = graphene.Field(TeaType)

    @auth_required
    def mutate(self, info, **kwargs):
        tea = Tea.objects.create(**kwargs, user=info.context.user)

        return CreateTea(tea=tea)