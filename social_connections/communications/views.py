from django.db.models import Count
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Communication
from .serializers import CommunicationSerializer
from .services import get_graph_communication


class GraphCommunication(APIView):

    def get(self, request):
        communications = Communication.objects.values('initiator_user', 'acceptor_user').annotate(total=Count('acceptor_user'))
        graph_info = get_graph_communication(communications)
        return Response({'graph': graph_info}, status=200)


class UserCommunications(APIView):

    def post(self, request):
        serializer = CommunicationSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': 'success', 'data': f'Новых записей: {len(serializer.data)}'}, status=201)
