"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rickhouseapi.models import Distillery, Whiskey, WhiskeyDistillery


class DistilleryView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        distillery = Distillery.objects.get(pk=pk)
        whiskey = Whiskey.objects.filter(
        joined_whiskey__distillery_id = distillery)
        distillery.whiskey.set(whiskey)
        serializer = DistillerySerializer(distillery, context={'distillery': distillery})
        return Response(serializer.data)


    def list(self, request):
        distilleries = Distillery.objects.all()
        whiskey = request.query_params.get('whiskey', None)
        if whiskey is not None: 
            whiskeys = whiskeys.filter(whiskey_id=whiskey)
            whiskey = request.query_params.get('whiskey_id', None)
        serializer = DistillerySerializer(distilleries, many=True)
        return Response(serializer.data)
    
    def destroy(self, request, pk):
        distillery = Distillery.objects.get(pk=pk)
        distillery.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class WhiskeyDistillerySerializer(serializers.ModelSerializer):
    class Meta:
        model = WhiskeyDistillery
        fields = ('id', )
        
class WhiskeySerializer(serializers.ModelSerializer):
    joined_whiskey = serializers.SerializerMethodField()
    class Meta:
        model = Whiskey
        fields = ('id', 'label', 'year', 'proof', 'type', 'joined_whiskey' )
    def get_joined_whiskey(self, obj):
        distillery = self.context.get('distillery')
        whiskeydistilleries = obj.joined_whiskey.filter(distillery=distillery)
        serializer = WhiskeyDistillerySerializer(whiskeydistilleries, many = True)
        return serializer.data

class DistillerySerializer(serializers.ModelSerializer):
    whiskey = WhiskeySerializer(many = True)
    class Meta:
        model = Distillery
        fields = ('id', 'name', 'whiskey')
        depth = 2
        