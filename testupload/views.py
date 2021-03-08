from django.shortcuts import render, redirect
from .models import TestModel


def upload_view(request):
    if request.method == "GET":
        return render(request, 'testupload/upload_view.html')
    else:
        print(request.POST)
        print(request.FILES.getlist('images'))
        image = request.FILES['images']
        a = TestModel.objects.create(image=image)
        a.save()
        return redirect('upload')