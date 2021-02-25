from django.core.serializers import serialize
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from api import serializers as api_serializers
from api import models as api_models
from rest_framework.permissions import IsAuthenticated


class Stock_En_TiendaViewSet(ViewSet):
    '''

    '''
    #import pdb
    # pdb.set_trace()
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = api_models.Stock_En_Tienda.objects.order_by('pk')
        serializer = api_serializers.Stock_En_TiendaSerializer(
            queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        datas = request.data
        datas = request.data
        lista_tiendas = [api_models.Stock_En_Tienda(**vals) for vals in datas]
        create = api_models.Stock_En_Tienda.objects.bulk_create(
            lista_tiendas)

        return Response({"Message": "Okay"})

    def retrieve(self, request, pk=None):
        queryset = api_models.Stock_En_Tienda.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = api_serializers.Stock_En_TiendaSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = api_models.Stock_En_Tienda.objects.get(pk=pk)
        except api_models.Stock_En_Tienda.DoesNotExist:
            return Response(status=404)
        serializer = api_serializers.Stock_En_TiendaSerializer(
            item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = api_models.Stock_En_Tienda.objects.get(pk=pk)
        except api_models.Stock_En_Tienda.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class TiendaViewSet(ViewSet):
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = api_models.Tienda.objects.order_by('pk')
        serializer = api_serializers.TiendaSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = api_serializers.TiendaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = api_models.Tienda.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = api_serializers.TiendaSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = api_models.Tienda.objects.get(pk=pk)
        except api_models.Tienda.DoesNotExist:
            return Response(status=404)
        serializer = api_serializers.TiendaSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = api_models.Tienda.objects.get(pk=pk)
        except api_models.Tienda.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class CategoriaViewSet(ViewSet):
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = api_models.Categoria.objects.order_by('pk')
        serializer = api_serializers.CategoriaSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = api_serializers.CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = api_models.Categoria.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = api_serializers.CategoriaSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = api_models.Categoria.objects.get(pk=pk)
        except api_models.Categoria.DoesNotExist:
            return Response(status=404)
        serializer = api_serializers.CategoriaSerializer(
            item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = api_models.Categoria.objects.get(pk=pk)
        except api_models.Categoria.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class SubCategoriaViewSet(ViewSet):
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = api_models.SubCategoria.objects.order_by('pk')
        serializer = api_serializers.SubCategoriaSerializer(
            queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = api_serializers.SubCategoriaSerializer(data=request.data)
        data = request.data
        if serializer.is_valid():
            create = api_models.SubCategoria.objects.create(
                nombre=data.get("nombre", ""),
                descripcion=data.get("descripcion", ""),
                icono=data.get("icono", None),
                categoria_id=data.get("categoria", "")
            )
            return Response({"id": create.id})
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = api_models.SubCategoria.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = api_serializers.SubCategoriaSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = api_models.SubCategoria.objects.get(pk=pk)
        except api_models.SubCategoria.DoesNotExist:
            return Response(status=404)
        serializer = api_serializers.SubCategoriaSerializer(
            item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = api_models.SubCategoria.objects.get(pk=pk)
        except api_models.SubCategoria.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class ProductoViewSet(ViewSet):
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = api_models.Producto.objects.order_by('pk')
        serializer = api_serializers.ProductoSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = api_serializers.ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = api_models.Producto.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = api_serializers.ProductoSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = api_models.Producto.objects.get(pk=pk)
        except api_models.Producto.DoesNotExist:
            return Response(status=404)
        serializer = api_serializers.ProductoSerializer(
            item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = api_models.Producto.objects.get(pk=pk)
        except api_models.Producto.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)
