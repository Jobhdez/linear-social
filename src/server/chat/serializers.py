from rest_framework import serializers
from api.models import BookStudy

class BookStudySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookStudy
        fields = ['owner', 'members', 'name']
