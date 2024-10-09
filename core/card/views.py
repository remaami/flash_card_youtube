from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from card.serializers import (
     CreateFlashCaredSerializer,
     UpdateFlashCaredSerializer,
     ListFlashCardserializer,
)
from rest_framework.response import Response
from rest_framework import status
from card.models import FlashCard
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

class CreateFlashCardView(APIView):
    def post(self, request):
        permission_classes=(IsAuthenticated,)
        serializer = CreateFlashCaredSerializer(data=request.data)
        serializer.is_valid(raise_exception=True,)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UpdateFlashCardView(APIView):
    def put(self, request, id):
        permission_classes=(IsAuthenticated,)
        quryset = get_object_or_404(FlashCard, id=id)
        serializer =UpdateFlashCaredSerializer(data=request.data, instance=quryset,)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

class DeleteFlashCardView(APIView):
    def delete(self, request, id):
        permission_classes=(IsAuthenticated,)
        quryset = get_object_or_404(FlashCard, id=id)
        quryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  

class ListFlashcardView(APIView):

     def get(self, request, user_id):
        permission_classes=(IsAuthenticated,)
        get_list_flashcard = get_list_or_404(FlashCard, user__id=user_id)
        serializer = ListFlashCardserializer(instance=get_list_flashcard, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
                 


