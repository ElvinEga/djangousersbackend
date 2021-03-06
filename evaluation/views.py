from evaluation.models import Evaluation, Question

__all__ = ['create_evaluation', 'create_question']

from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import Permission
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import make_password
from django.contrib.auth.signals import user_logged_in
from django.db.models import Q

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes

# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny, ])
def create_evaluation(request):
    """
    Endpoint: /users/create_user/
    Method: POST
    Allowed users: All user
    Response status code: 201 created
    Description: admin can create users of a
    """

  #  if not request.user.has_perm('users.add_user'):
   #     return Response({'error': 'can not create user'}, status=status.HTTP_403_FORBIDDEN)


    evaluation_details = request.data

    eval = Evaluation(
        lec_id=evaluation_details['lec_id'],
        student_id=evaluation_details['stud_id'],

    )
    eval.save()
    eval_details = {}
    eval_details['evaluation_id'] = eval.id



   # return Response({'success': "user added successfully"}, status=status.HTTP_201_CREATED)
    return Response(eval_details, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([AllowAny, ])
def create_question(request):
    """
    Endpoint: /users/create_user/
    Method: POST
    Allowed users: All user
    Response status code: 201 created
    Description: admin can create users of a
    """

  #  if not request.user.has_perm('users.add_user'):
   #     return Response({'error': 'can not create user'}, status=status.HTTP_403_FORBIDDEN)


    question_details = request.data

    que = Question(
        question=question_details['question'],
        category=question_details['category'],
        evaluation_id=question_details['evaluation_id'],
        rating=question_details['rating']

    )
    que.save()



    return Response({'success': "user added successfully"}, status=status.HTTP_201_CREATED)
    #return Response(eval_details, status=status.HTTP_201_CREATED)