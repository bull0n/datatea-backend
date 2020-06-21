
import graphene
import teas.schema

class Query(teas.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
