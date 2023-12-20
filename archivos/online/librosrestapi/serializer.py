from.models import LibrosRestApi
from rest_framework import serializers


class LibrosRestApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibrosRestApi
        fields = '__all__'



