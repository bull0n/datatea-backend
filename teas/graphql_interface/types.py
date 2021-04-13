import graphene
from graphene_django.types import DjangoObjectType

from teas.models import Tea

class TeaType(DjangoObjectType):
    category_label = graphene.String()

    class Meta:
        model = Tea

    def resolve_category_label(self, info):
        return self.get_category_display()

