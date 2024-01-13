from django.http import JsonResponse
from django.views.generic import View
from .models import UserFollowing
from django.contrib.auth.models import User

# Create your views here.
class AddFollowerView(View):

    def post(self, request, *args, **kwargs):
        user = User.objects.get(id=int(request.POST["user"][0]))
        follower = User.objects.get(id=int(request.POST['follower'][0]))
        UserFollowing.objects.create(user_id=user,following_user_id=follower)
        return JsonResponse({'success': True})