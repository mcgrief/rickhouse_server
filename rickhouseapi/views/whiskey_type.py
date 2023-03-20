"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rickhouseapi.models import Type


class TypeView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        whiskey_type = Type.objects.get(pk=pk)
        serializer = TypeSerializer(whiskey_type)
        return Response(serializer.data)


    def list(self, request):
        whiskey_types = Type.objects.all()
        serializer = TypeSerializer(whiskey_types, many=True)
        return Response(serializer.data)

class TypeSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Type
        fields = ('id', 'name')