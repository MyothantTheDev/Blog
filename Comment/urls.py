from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import NewComment,CommentList

urlpatterns = [
    path('new', NewComment.as_view(), name='comment.new'),
    path('commentlist', CommentList.as_view(), name='comment.list'),
]