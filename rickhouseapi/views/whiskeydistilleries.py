"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rickhouseapi.models import WhiskeyDistillery, Whiskey, Distillery


class WhiskeyDistilleryView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        whiskeydistillery = WhiskeyDistillery.objects.get(pk=pk)
        serializer = WhiskeyDistillerySerializer(whiskeydistillery)
        return Response(serializer.data)


    def list(self, request):
        whiskeydistilleries = WhiskeyDistillery.objects.all()
        distillerywhiskey = request.query_params.get('distillery', None)
        if distillerywhiskey is not None:
            whiskeydistilleries.filter(distillery=distillerywhiskey)
        serializer = WhiskeyDistillerySerializer(whiskeydistilleries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        whiskey = Whiskey.objects.get(pk=request.data["whiskey_id"])
        distillery = Distillery.objects.get(pk=request.data["distillery_id"])
        whiskeydistillery = WhiskeyDistillery.objects.create(
            whiskey = whiskey,
            distillery = distillery
        )
        serializer = WhiskeyDistillerySerializer(whiskeydistillery)
        return Response(serializer.data)

class WhiskeyDistillerySerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = WhiskeyDistillery
        fields = ('id', 'whiskey', 'distillery')
        depth= 2