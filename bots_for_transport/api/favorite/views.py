from bot.models import Bot
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from favorite.models import Favorite
from favorite.serializers import FavoriteSerializer, FavoriteListSerializer
from api.pagination import LimitPageNumberPagination


class FavoriteListView(ListAPIView):
    serializer_class = FavoriteListSerializer

    def get_queryset(self):
        user = self.request.user.id
        return Favorite.objects.filter(user=user)



class FavoriteView(APIView):

    permission_classes = [IsAuthenticated, ]
    pagination_class = LimitPageNumberPagination

    def post(self, request, id):
        context = {'request': request}
        bot = get_object_or_404(Bot, id=id)
        data = {
            'user': request.user.id,
            'bot': bot.id
        }
        serializer = FavoriteSerializer(data=data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, id):
        shopping_cart = Favorite.objects.filter(
            user=request.user.id,
            bot=get_object_or_404(Bot, id=id)
        )
        shopping_cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
