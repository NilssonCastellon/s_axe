from rest_framework.response import Response #para responder
from .models import evaluacion
from .seriealizers import evaluacionSerializer
from rest_framework.decorators import api_view
from rest_framework import status

from django.db import connection

@api_view(['GET', 'POST']) #Le indicamos que metodos tenemos permitidos para esa funcion
def evaluacion_api_view(request):
    #list
    if request.method == 'GET':
        #queryset
        evaluacion = evaluacion.objects.all() #todos los registros
        evaluacion_serializer = evaluacionSerializer(evaluacion, many = True) #Indicamos many, porque es un listado, no solo uno   

        return Response(evaluacion_serializer.data, status = status.HTTP_200_OK)
    
    elif request.method == 'POST':
        request.data['cod_eva'] 
        permiso_serializer = evaluacionSerializer(data= request.data)#
        
        cod_eva = request.data.get('cod_eva') #Extraemos el codigo del rol, para el que crearemos permosos

        if evaluacion_serializer.is_valid(): #Revisar que sucede cuando no es valido
           cursor = connection.cursor()

           cod_eva = request.data.get('cod_eva')
           institucion = request.data.get('institucion')
           municipio = request.data.get('municipio')
           detalle = request.data.get('detalle')
           estado = request.data.get('estado')
           cursor.execute("Select sp_evaluacion('I', %s, %s, %s, %s, %s)", [cod_eva,institucion,municipio,detalle,estado])
           cursor.close() #para cerrar la conexion a base de datos

           return Response({'message':'¡Usuario creado correctamente!'}, status = status.HTTP_201_CREATED) #Envia los datos actualizados
        else:
            print(permiso_serializer.errors)       

        return Response({'message':'¡Ha ocurrido algo inesperado!'}, status= status.HTTP_400_BAD_REQUEST) #Si existen errores, los devuelve
    

@api_view(['GET', 'PUT'])
def evaluacion_detalle_api_view(request, pk = None): #pk 2
    evaluacion = evaluacion.objects.filter(COD_EVA = pk).first()  
    if evaluacion:
        if request.method == 'GET':

            evaluacion_serializer = evaluacionSerializer(evaluacion)        

            return Response(evaluacion_serializer.data, status = status.HTTP_200_OK)

        elif request.method == 'PUT':
                evaluacion_permiso = request.data.get('COD_EVA')

                #Llamamos el registro a modificar
                evaluacion = evaluacion.objects.filter(COD_EVA =  evaluacion_permiso).first() 

                evaluacion_serializer = evaluacionSerializer(evaluacion, data = request.data)
                if evaluacion_serializer.is_valid():
                    cursor = connection.cursor()

                    

                    cod_eva = request.data.get('cod_eva')
                    institucion = request.data.get('institucion')
                    municipio = request.data.get('municipio')
                    detalle = request.data.get('detalle')
                    estado = request.data.get('estado')
                    cursor.execute("Select sp_evaluacion('U', %s, %s, %s, %s, %s)", [cod_eva,institucion,municipio,detalle,estado])
                    cursor.close() #para cerrar la conexion a base de dato
                    
                    return Response({'message':'¡Usuario actualizado correctamente!'}, status = status.HTTP_201_CREATED) #Envia los datos actualizados)
                else:
                    return Response(evaluacion_serializer.errors, status= status.HTTP_400_BAD_REQUEST)
