from rest_framework import serializers
from .models import LinearAlgebraExpression

class LinearAlgebraExpSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinearAlgebraExpression
        fields = ['exp', 'user_name']
