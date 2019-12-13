from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

@csrf_exempt
def simple_upload(request):
    if request.method == 'POST' and request.FILES['file']:

        file = request.FILES['file']
        if file._size > settings.MAX_UPLOAD_SIZE:
            return HttpResponse("File too large")

        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        uploaded_file_url = fs.url(filename)
        return HttpResponse(uploaded_file_url)
    return HttpResponse("false")
