
import graphene
import graphql_jwt
import teas.schema

class Query(teas.schema.Query, graphene.ObjectType):
    pass

class Mutation(teas.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
