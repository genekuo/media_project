from PIL import Image
from django.conf import settings
from django.shortcuts import render

from .forms import UploadForm


def media_example(request):
    instance = None
    save_path = None
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            save_path = settings.MEDIA_ROOT / form.cleaned_data["file_upload"].name
            print(save_path)
            image = Image.open(form.cleaned_data["file_upload"])
            print(image.width)
            print(image.height)
            #image.thumbnail((500, 400))
            print(image.info['dpi'])
            image_1 = image.resize((500, 400))
            print(image_1.width)
            print(image_1.height)
            print(image_1.info['dpi'])
            image_1.save(save_path)
            
            instance = form.save()

    else:
        form = UploadForm()

    #return render(request, "media-example.html", {"form": form})
    return render(request, "media-example.html", {"form": form, "instance": instance})
