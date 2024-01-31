from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import google.generativeai as genai
import PIL.Image
from .models import Test
from .forms import ImageForm
@csrf_exempt
def upload_image(request):
    if request.method == 'POST':
        response=""
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image=request.FILES["image_file"]
            genai.configure(api_key="AIzaSyD0qQm-WS-Uyb7F9Pdj_oivinzlaPdtZTs")
            img1 = PIL.Image.open(image)
            model = genai.GenerativeModel('gemini-pro-vision')
            response = model.generate_content(img1)
            form.save()
        else:
            response="invalid form"  
        return HttpResponse(response.text)
