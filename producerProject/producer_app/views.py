from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Message
from .tasks import process_data
from .serializers import MessageSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_api_key.permissions import HasAPIKey


@api_view(['POST'])
@permission_classes([HasAPIKey])
def webhook_receiver(request):
    """
    Receives data from the consumer via a webhook and updates the message model.

    Expects a JSON payload with a 'text' field.
    """
    data = request.data
    text = data.get('text')
    if text:
        message = Message.objects.create(text=text)
        serializer = MessageSerializer(message)
        return Response(serializer.data, status=201)
    else:
        return Response({'error': 'Invalid data'}, status=400)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    #authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
