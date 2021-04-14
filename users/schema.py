import graphql_jwt
import graphene
from .graphql_interface.queries import UsersQuery

class Mutation(object):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


class Query(UsersQuery, graphene.ObjectType):
    pass