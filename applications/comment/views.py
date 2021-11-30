from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from applications.comment.models import Comment, Like
from applications.comment.permissions import IsCommentAuthor
from applications.comment.serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permissions = []
        elif self.action == 'like':
            permissions = [IsAuthenticated, ]
        else:
            permissions = [IsCommentAuthor, ]
        return [permission() for permission in permissions]

    @action(detail=True, methods=['POST'])
    def like(self, request, *args, **kwargs):
        comment = self.get_object()
        like_obj, _ = Like.objects.get_or_create(comment=comment, user=request.user)
        like_obj.like = not like_obj.like
        like_obj.save()
        status = 'liked'
        if not like_obj.like:
            status = 'unliked'
        return Response({'status': status})

    def get_serializer_context(self):
        return {'request': self.request}
