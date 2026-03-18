from django.shortcuts import render

from lms.app1.models import MyModel

# Create your views here.
def cnt (request):
    count = MyModel.objects.all().count()
    print(count)
    return render(f"total course are {count}")