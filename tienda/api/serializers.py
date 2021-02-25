from rest_framework.serializers import ModelSerializer
from api.models import Stock_En_Tienda, Tienda, Categoria, SubCategoria, Producto


class Stock_En_TiendaSerializer(ModelSerializer):

    class Meta:
        model = Stock_En_Tienda
        depth = 2
        fields = '__all__'


class TiendaSerializer(ModelSerializer):

    class Meta:
        model = Tienda
        depth = 2
        fields = '__all__'


class CategoriaSerializer(ModelSerializer):

    class Meta:
        model = Categoria
        depth = 2
        fields = '__all__'


class SubCategoriaSerializer(ModelSerializer):

    class Meta:
        model = SubCategoria
        depth = 2
        fields = '__all__'


class ProductoSerializer(ModelSerializer):

    class Meta:
        model = Producto
        depth = 2
        fields = '__all__'
