import graphene
from django.core.exceptions import FieldDoesNotExist

from .types import TeaType, CategoryEnum, StatusEnum
from teas.models import Tea
from users.decorators import auth_required

class CreateTea(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
        name = graphene.String(required=True)
        category = graphene.Argument(CategoryEnum, required=True)
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
        tea = Tea.objects.update_or_create(**kwargs, user=info.context.user)

        return CreateTea(tea=tea)

class UpdateTeaStatus(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        status = graphene.Argument(StatusEnum, required=True)

    ok = graphene.Boolean()

    @auth_required
    def mutate(self, info, id, status):
        affected_rows = Tea.objects.filter(pk=id).update(status=status)

        if affected_rows == 0:
            raise FieldDoesNotExist(f'Tea with id={id} does not exist')

        return UpdateTeaStatus(ok=affected_rows > 0)