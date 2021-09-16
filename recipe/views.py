from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import RecipeSerializer
from .models import Recipe
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class RecipeList(ListCreateAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeDetail(RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
