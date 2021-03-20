from teas.graphql_interface.mutations import CreateTea
from teas.graphql_interface.queries import TeasQuery
from teas.models import Tea
import graphene

class Mutation(object): 
    create_tea = CreateTea.Field()
    pass

class Query(TeasQuery, graphene.ObjectType):
    pass