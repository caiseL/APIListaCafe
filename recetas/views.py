from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import RecetaSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Receta

@api_view(['GET'])
def api_root(request):
    return Response({'recetas' : 
    
    reverse('lista-recetas', request=request, format=None),
    })


# Paginación?
class ListaRecetas(ListAPIView):
    serializer_class = RecetaSerializer
    queryset = Receta.objects.all()

class CrearReceta(CreateAPIView):
    serializer_class = RecetaSerializer