from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import QuoteCard
from .serializers import QuoteCardSerializer


class QuotePage(APIView):
    
    @api_view(['GET', 'POST'])


    def quoteList(request, format=None):


        if request.method == 'GET':
            data_model = QuoteCard.objects.all()
            serializer = QuoteCardSerializer(data_model, many=True)
            return Response(serializer.data)
        


        if request.method == 'POST':
            serializer = QuoteCardSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(['GET', 'PUT', 'DELETE'])


    def quoteFunctionality(request,id,format=None):
        
        try:
            modelData = QuoteCard.objects.get(pk=id)
        except QuoteCard.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        

        if request.method == 'GET':
            serializer = QuoteCardSerializer(modelData)
            return Response(serializer.data)


        if request.method == 'PUT':
            serializer = QuoteCardSerializer(modelData, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)


        elif request.method == 'DELETE':
            modelData.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
