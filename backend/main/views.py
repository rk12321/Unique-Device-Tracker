from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Users

def index(request):
    return HttpResponse("Hello Geeks")

@csrf_exempt
def store(request, device_id):
    try:
        visitor = Users.objects.get(device_id=device_id)
        visitor.visits += 1
        visitor.save()
        return JsonResponse({'exists': True})
    except Users.DoesNotExist:
        new_visitor = Users.objects.create(device_id=device_id, visits=0)
        return JsonResponse({'exists': False})  
