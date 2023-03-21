from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
from pantries.models import Recipe, Ingredient, Quantity, Unit, Info, Nutrition
from .serializers import RecipeSerializer, IngredientSerializer, QuantitySerializer, UnitSerializer, InfoSerializer, NutritionSerializer


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_recipes': 'recipes/',
        'all_ingredients': 'ingredients/',
        'all_quantities': 'quantities/',
        'all_units': 'units/',
        'all_nutrition': 'nutrition/',
        'all_info': 'info/'
    }

    return Response(api_urls)


@api_view(['GET'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
def view_recipes(request):

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


@api_view(['GET'])
def view_quantities(request):

    if request.query_params:
        items = Quantity.objects.filter(**request.query_params.dict())
    else:
        items = Quantity.objects.all()

    if items:
        return Response(QuantitySerializer(items, many=True).data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_units(request):

    if request.query_params:
        items = Unit.objects.filter(**request.query_params.dict())
    else:
        items = Unit.objects.all()

    if items:
        return Response(UnitSerializer(items, many=True).data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_nutrition(request):

    if request.query_params:
        items = Nutrition.objects.filter(**request.query_params.dict())
    else:
        items = Nutrition.objects.all()

    if items:
        return Response(NutritionSerializer(items, many=True).data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_info(request):

    if request.query_params:
        items = Info.objects.filter(**request.query_params.dict())
    else:
        items = Info.objects.all()

    if items:
        return Response(InfoSerializer(items, many=True).data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
