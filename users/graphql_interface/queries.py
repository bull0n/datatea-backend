import graphene
from .types import UserType
from django.contrib.auth.models import User

class UsersQuery(object):
    user = graphene.Field(UserType, id=graphene.Int())
            
    def resolve_user(self, info, id):
        if id is not None:
            return User.objects.get(pk=id)

        return None