from django.urls import path
from .views import RecipeList, RecipeDetail

urlpatterns = [
    path("", RecipeList.as_view(), name="Recipe_list"),
    path("<int:pk>/", RecipeDetail.as_view(), name="Recipe_detail"),
]
