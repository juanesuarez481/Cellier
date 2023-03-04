from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
from pantries.models import Recipe, Ingredient
from .serializers import RecipeSerializer, IngredientSerializer


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_recipes': 'all/',
        'all_ingredients': 'ingredients/',
    }

    return Response(api_urls)


@api_view(['GET'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
def view_items(request):

    if request.query_params:
        items = Recipe.objects.filter(**request.query_params.dict())
    else:
        items = Recipe.objects.all()

    if items:
        return Response(RecipeSerializer(items, many=True).data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_ingredients(request):

    if request.query_params:
        items = Ingredient.objects.filter(**request.query_params.dict())
    else:
        items = Ingredient.objects.all()

    if items:
        return Response(IngredientSerializer(items, many=True).data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
