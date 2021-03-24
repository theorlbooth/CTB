from ..serializers.common import SaleSerializer
from jwt_auth.serializers.common import NestedUserSerializer
from beers.serializers.common import NestedBeerSerializer

class PopulatedSaleSerializer(SaleSerializer):

    user = NestedUserSerializer()
    beer = NestedBeerSerializer()
    