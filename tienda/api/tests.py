import tempfile

from django.contrib.auth import get_user_model
from PIL import Image
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from api import models as tienda_models
import logging
logging.disable(logging.CRITICAL)


class TestCaseStock(APITestCase):
    def setUp(self):
        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()
        self.client.defaults['HTTP_AUTHORIZATION'] = 'Token {}'.format(
            self.token.key)

    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user(
            'test',
            email='testuser@test.com',
            password='test'
        )

    def image(self):
        super().setUp()
        self.file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image = Image.new('RGB', (100, 100))
        image.save(self.file.name)
        return self.file

    def test_producto(self):
        '''
        Testing Producto Model
        '''
        data = {
            "nombre": "test",
            "presentacion": "test",
            "marca": "test",
            "fabricante": "test",
            "foto": self.image(),
            "descripcion": "test",
            "nivel_azucar": "test",
            "nivel_sal": "test",
            "nivel_grasa": "test",
            "estado": "test"
        }
        producto = self.client.post('/api/producto/', data, format='multipart')
        data = {
            "nombre": "test",
            "presentacion": "test",
            "marca": "test",
            "fabricante": "test",
            "foto": self.image(),
            "descripcion": "test",
            "nivel_azucar": "test",
            "nivel_sal": "test",
            "nivel_grasa": "test",
            "estado": "test"
        }
        producto = self.client.post('/api/producto/', data, format='multipart')
        ret = self.client.get('/api/producto/', format='json',
                              HTTP_AUTHORIZATION='Token {}'.format(self.token.key))
        self.assertEqual(tienda_models.Producto.objects.all().count(), 2)
        ret = self.client.get(
            f'/api/producto/{producto.data["id"]}/', format='json')
        self.assertEqual(ret.data['id'], 2)

        '''
        Testing Categoria Model
        '''

        data = {
            "nombre": "test",
            "descripcion": "test",
            "icono": self.image(),
        }
        categoria = self.client.post(
            '/api/categoria/', data, format='multipart')
        ret = self.client.get(
            f'/api/categoria/{categoria.data["id"]}/', format='json')
        self.assertEqual(tienda_models.Categoria.objects.all().count(), 1)
        self.assertEqual(ret.data['id'], 1)
        data = {
            "nombre": "test",
            "descripcion": "test",
            "icono": self.image(),
        }
        categoria = self.client.post(
            '/api/categoria/', data, format='multipart')
        ret = self.client.get(
            f'/api/categoria/{categoria.data["id"]}/', format='json')
        self.assertEqual(tienda_models.Categoria.objects.all().count(), 2)
        self.assertEqual(ret.data['id'], 2)

        '''
        Testing SubCategoria Model
        '''

        data = {
            "nombre": "test",
            "descripcion": "test",
            "icono": self.image(),
            "categoria": categoria.data["id"]
        }
        subcategoria = self.client.post(
            '/api/subcategoria/', data, format='multipart')
        ret = self.client.get(
            f'/api/subcategoria/{subcategoria.data["id"]}/', format='json')
        self.assertEqual(tienda_models.SubCategoria.objects.all().count(), 1)
        self.assertEqual(ret.data['id'], 1)
        data = {
            "nombre": "test",
            "descripcion": "test",
            "icono": self.image(),
            "categoria": categoria.data["id"]
        }
        subcategoria = self.client.post(
            '/api/subcategoria/', data, format='multipart')
        ret = self.client.get(
            f'/api/subcategoria/{subcategoria.data["id"]}/', format='json')
        self.assertEqual(tienda_models.SubCategoria.objects.all().count(), 2)
        self.assertEqual(ret.data['id'], 2)
        '''
        Testing Tienda Model
        '''

        data = {
            "id_ciudad": "test",
            "nombre": "test",
            "logo": self.image(),
        }
        tienda = self.client.post('/api/tienda/', data, format='multipart',
                                  HTTP_AUTHORIZATION='Token {}'.format(self.token.key))
        ret = self.client.get(
            f'/api/tienda/{tienda.data["id"]}/', format='json')
        self.assertEqual(tienda_models.Tienda.objects.all().count(), 1)
        self.assertEqual(ret.data['id'], 1)

        data = {
            "id_ciudad": "test",
            "nombre": "test",
            "logo": self.image(),
        }
        tienda = self.client.post('/api/tienda/', data, format='multipart',
                                  HTTP_AUTHORIZATION='Token {}'.format(self.token.key))
        ret = self.client.get(
            f'/api/tienda/{tienda.data["id"]}/', format='json')
        self.assertEqual(tienda_models.Tienda.objects.all().count(), 2)
        self.assertEqual(ret.data['id'], 2)

        '''
        Testing Stock_En_Tienda Model
        '''
        data = []
        how_many_elem = 150000
        import logging
        import time
        for index in range(0, how_many_elem):
            data.append({
                "pvp": 1.0,
                "tiene_iva": True,
                "estado": "published",
                "precio_compra": 1.0,
                "margen_ganancia": 1.0,
                "id_tienda": tienda.data["id"],
                "id_producto": producto.data["id"],
                "categoria_id": categoria.data["id"]
            })
        tiempo_inicial = time.time()
        self.client.post(
            '/api/stock_en_tienda/', data=data, format='json')
        print(time.time()-tiempo_inicial, ", en enviar el post con 150.000 objetos de Stock_En_Tienda")
        self.assertEqual(
            tienda_models.Stock_En_Tienda.objects.all().count(), how_many_elem)
        '''
        Testing Delete
        '''
        ret = self.client.delete(
            f'/api/stock_en_tienda/{tienda_models.Stock_En_Tienda.objects.all().first().id}/', format='json')
        self.assertEqual(
            tienda_models.Stock_En_Tienda.objects.all().count(), how_many_elem-1)
        ret = self.client.delete(
            f'/api/subcategoria/{subcategoria.data["id"]}/', format='json')
        self.assertEqual(tienda_models.SubCategoria.objects.all().count(), 1)
        tienda_models.SubCategoria.objects.all().delete()
        ret = self.client.delete(
            f'/api/categoria/{categoria.data["id"]}/', format='json')
        self.assertEqual(tienda_models.Categoria.objects.all().count(), 1)
        ret = self.client.delete(
            f'/api/producto/{producto.data["id"]}/', format='json')
        self.assertEqual(tienda_models.Producto.objects.all().count(), 1)
        ret = self.client.delete(
            f'/api/tienda/{tienda.data["id"]}/', format='json')
        self.assertEqual(tienda_models.Tienda.objects.all().count(), 1)
