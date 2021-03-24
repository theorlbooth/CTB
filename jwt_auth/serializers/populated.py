from ..serializers.common import UserSerializer
from beers.serializers.common import BeerSerializer
from sales.serializers.common import SaleSerializer

class PopulatedUserSerializer(UserSerializer):

    sales = SaleSerializer(many=True)
    