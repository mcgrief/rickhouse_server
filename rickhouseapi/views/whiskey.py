"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rickhouseapi.models import Whiskey, User, Type


class WhiskeyView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        whiskey = Whiskey.objects.get(pk=pk)
        serializer = WhiskeySerializer(whiskey)
        return Response(serializer.data)

    def list(self, request):
        whiskey = Whiskey.objects.all()
        serializer = WhiskeySerializer(whiskey, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        user = User.objects.get(pk=request.data["user"])
        type = Type.objects.get(pk=request.data["type"])

        whiskey = Whiskey.objects.create(
        label=request.data["label"],
        year=request.data["year"],
        proof=request.data["proof"],
        user=user,
        type=type,
    )
        serializer = WhiskeySerializer(whiskey)
        return Response(serializer.data)
    
    def update(self, request, pk):
        type = Type.objects.get(pk=request.data["type"])
        whiskey = Whiskey.objects.get(pk=pk)
        whiskey.label = request.data["label"]
        whiskey.year = request.data["year"]
        whiskey.proof = request.data["proof"]

        whiskey.type = type
        whiskey.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        whiskey = Whiskey.objects.get(pk=pk)
        whiskey.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)



class WhiskeySerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Whiskey
        fields = ('user', 'label', 'proof', 'year', 'type', 'id')
        depth = 2
        