from rest_framework.viewsets import ModelViewSet
from .serializers import BotSerializer
from .models import Bot


class BotViewSet(ModelViewSet):
    queryset = Bot.objects.all()
    serializer_class = BotSerializer
