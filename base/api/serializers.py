from rest_framework.serializers import ModelSerializer
from base.models import Room

class RoomsSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


