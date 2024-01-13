from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.decorators.clickjacking import xframe_options_sameorigin
from .views import NewComment

urlpatterns = [
    path('new/', NewComment.as_view(), name='comment.new'),
    # path('commentlist/<id>', xframe_options_sameorigin(CommentList.as_view()), name='comment.list'),
]