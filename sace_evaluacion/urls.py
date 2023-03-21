from django.urls import path
#from apps.users.api.api import UserAPIView
from .api import evaluacion_api_view, evaluacion_detalle_api_view

urlpatterns = [
    path('datos/', evaluacion_api_view, name='evaluacion'),
    path('datos/<int:pk>', evaluacion_detalle_api_view, name='evaluacion_detalle')
    #path('usuario/', UserAPIView.as_view(), name='usuario_api')
]
