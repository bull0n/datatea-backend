
from teas.models import Tea
from .types import TeaType
import graphene
from graphql import GraphQLError
from users.decorators import auth_required

class TeasQuery(object):
    teas = graphene.List(TeaType)

    tea = graphene.Field(TeaType,
                        id=graphene.Int(),
                        name=graphene.String())

    @auth_required
    def resolve_teas(self, info, **kwargs):
        print(Tea.objects.all())
        return Tea.objects.all()

    def resolve_tea(self, info, **kwargs):

        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Tea.objects.get(pk=id)

        if name is not None:
            return Tea.objects.get(name=name)

        return None


