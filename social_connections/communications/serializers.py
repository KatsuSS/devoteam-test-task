from rest_framework import serializers

from .models import Communication


class CommunicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Communication
        fields = ('initiator_user', 'acceptor_user',)
