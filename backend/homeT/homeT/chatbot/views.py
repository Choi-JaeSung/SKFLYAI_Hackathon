from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .chatbot_model_v1 import chatbot_model
from .chatbot_model_v2 import chatbot_model5


@api_view(['POST'])
def stt_response(request):
    if request.method == 'GET':
        print('GET Accepted')
    elif request.method == 'POST':
        data = request.data
        print(data)
        data['stt_Text'] = chatbot_model5(data['stt_Text'])
        print(data)
        return Response(data, status=status.HTTP_200_OK)
