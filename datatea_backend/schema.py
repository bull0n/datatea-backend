
import graphene
import teas.schema
import users.schema

class Query(teas.schema.Query, users.schema.Query, graphene.ObjectType):
    pass

class Mutation(teas.schema.Mutation, users.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
