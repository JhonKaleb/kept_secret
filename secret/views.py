from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import SecretSerializer, SecretHeaderSerializer, CommentSerializer
from .models import Secret, Comment

#class SecretViewSet(viewsets.ModelViewSet):
#     queryset = Secret.objects.all()
#     serializer_class = SecretSerializer


@api_view(['GET'])
def all_secrets(request):
    secrets = Secret.objects.all().values_list()
    return Response(secrets)

@api_view(['GET'])
def get_secret(request, secret_id):
    try:
        secret = Secret.objects.get(id=secret_id)
    except Secret.DoesNotExist:
       return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = SecretSerializer(secret)
    return Response(serializer.data)

@api_view(['PATCH'])
def hug(request, secret_id):
    try:
        secret = Secret.objects.get(id=secret_id)
    except Secret.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    secret.hugs += 1
    secret.save()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def create_secret(request):
    serializer = SecretSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def comment_secret(request, secret_id):
    request.data._mutable = True
    request.data['secret_id'] = secret_id
    request.data._mutable = False
    serializer = CommentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def like_comment(request, secret_id, coment_id):
    try:
        comment = Comment.objects.get(id=coment_id)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    comment.thanks += 1
    comment.save()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PATCH'])
def report_comment(request, secret_id, coment_id):
    try:
        comment = Comment.objects.get(id=coment_id)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    comment.reports += 1
    comment.save()
    return Response(status=status.HTTP_204_NO_CONTENT)