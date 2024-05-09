from rest_framework import serializers

from .models import SoleoDetails


class SoleoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoleoDetails
        fields = ['data']
