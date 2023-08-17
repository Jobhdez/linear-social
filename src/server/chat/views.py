from django.shortcuts import render
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from .serializers import BookStudySerializer

@api_view(['GET'])
@login_required
def study_chat_room(request, study_id):
    try:
        study_group = request.user.study_groups(id=study_id)
    except:
        return Response({"user": "not part of study group"})

    serializer = BookStudySerializer(study_group, many=True)
    
    return Response({'study group': serializer.data})
