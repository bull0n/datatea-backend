
import graphene
import teas.schema

class Query(teas.schema.Query, graphene.ObjectType):
    pass

class Mutation(teas.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
