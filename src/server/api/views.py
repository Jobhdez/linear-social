from django.shortcuts import render
from src.interpreter.parser import parser
from src.interpreter.interpreter import evaluate
from .forms import (
    UserRegistrationForm,
    LoginForm,
    RequestFriendForm,
    AcceptForm,
    LinearAlgebraExpForm,
    )
from .models import FriendRequest, LinearAlgebraExpression
from django.contrib.auth import (
    authenticate,
    login,
    get_user_model,
    )
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .serializers import LinearAlgebraExpSerializer
User = get_user_model()

@api_view(['POST'])
def register(request):
    """View that allows the given user register."""
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
        new_user = form.save(commit=False)
        data = form.cleaned_data
        new_user.set_password(data['password'])
        new_user.save()

        return Response({'account': 'created'})
    
    return Response({'form': 'invalid'})


@api_view(['POST'])
def user_login(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        username = data['username']
        password = data['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return Response({'login': 'Succesful'}) # should I respond with a status error?

        else:
            return Response({'Invalid': 'login'}) ## respond with a status error?

    else:
        return Response({'form': 'invalid'})

@api_view(['POST'])
@login_required(login_url='/api/login/')
@csrf_exempt
def request_friend(request):
    form = RequestFriendForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data  
        from_user = request.user
        to_user = User.objects.get(id=cd['id'])
        friend_request, created = FriendRequest.objects.get_or_create(from_user=from_user, to_user=to_user)

        if created:
            return Response({'request': 'sent'})
        else:
            return Response({'request': 'was sent already'})

@api_view(['POST'])
@login_required(login_url='/api/login/')
@csrf_exempt
def accept_friend_request(request):
    form = AcceptForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        friend_request = FriendRequest.objects.get(id=cd['id'])
        if friend_request.to_user == request.user:
            friend_request.to_user.friends.add(friend_request.from_user)
            friend_request.from_user.friends.add(friend_request.to_user)
            friend_request.delete()

            return Response({"accept": "request"})
        else:
            return Response({"request":"not accepted"})

@api_view(['POST'])
@login_required(login_url='/api/login/')
@csrf_exempt
def compute_lalg_expression(request):
    form = LinearAlgebraExpForm(request.POST)
    if form.is_valid():
        new_expr = form.save(commit=False)
        data_expr = form.cleaned_data
        data_expr = data_expr['exp']
        parsed_exp = parser.parse(data_expr)
        eval_data = evaluate(parsed_exp)
        expr_model = LinearAlgebraExpression(exp=eval_data)
        expr_model.save()
        serializer = LinearAlgebraExpSerializer(expr_model)

        return Response(serializer.data)
