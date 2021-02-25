from rest_framework.routers import SimpleRouter
from api import views
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path


router = SimpleRouter()

router.register(r'api/stock_en_tienda',
                views.Stock_En_TiendaViewSet, 'Stock_En_Tienda')
router.register(r'api/tienda', views.TiendaViewSet, 'Tienda')
router.register(r'api/categoria', views.CategoriaViewSet, 'Categoria')
router.register(r'api/subcategoria', views.SubCategoriaViewSet, 'SubCategoria')
router.register(r'api/producto', views.ProductoViewSet, 'Producto')

urlpatterns = router.urls
urlpatterns += [
    path('api-token-auth/', obtain_auth_token,
         name='api_token_auth'),
]
