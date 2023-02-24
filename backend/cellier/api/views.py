from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from pantries.models import Recipe
from .serializers import RecipeSerializer


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': 'all/',
    }

    return Response(api_urls)


@api_view(['GET'])
def view_items(request):

    if request.query_params:
        items = Recipe.objects.filter(**request.query_params.dict())
    else:
        items = Recipe.objects.all()

    if items:
        return Response(RecipeSerializer(items, many=True).data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
