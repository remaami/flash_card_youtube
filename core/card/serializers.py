from rest_framework.serializers import ModelSerializer
from card.models import FlashCard

class CreateFlashCaredSerializer(ModelSerializer):
    class Meta:
        model = FlashCard
        fields = "__all__"


class UpdateFlashCaredSerializer(ModelSerializer):
    class Meta:
        model = FlashCard
        fields = ("answer", "question")


class ListFlashCardserializer(ModelSerializer):

    class Meta:
        model = FlashCard
        fields = "__all__"                