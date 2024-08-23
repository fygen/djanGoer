from django.shortcuts import render

# Create your views here.
import os
from django.http import JsonResponse
from datetime import datetime
from PIL import Image
import pytesseract
import pyautogui
from django.conf import settings
from .interactServer.text_utils import setClipboard

def take_screen_and_get_text(request):
    # Define the region for the screenshot (left, top, width, height)
    left = request.GET.get('left', '0')
    top = request.GET.get('top', '0')
    width = request.GET.get('width', '1920')
    height = request.GET.get('height', '1080')
    lang = request.GET.get('language', 'eng')
    answer = request.GET.get('answer', "")
    if(len(answer)):
        print(answer)
        setClipboard(answer)
    # left = int(request.GET.get('left', 0))
    # top = int(request.GET.get('top', 0))
    # width = int(request.GET.get('width', 1920))
    # height = int(request.GET.get('height', 1080))
    # lang = str(request.GET.get('lang', 'tur'))

    # Define the region for the screenshot (left, top, width, height)
    region = (int(left), int(top), int(width), int(height))

    # Take a screenshot
    filename = str(datetime.now().strftime("%Y.%m.%d-%H.%M.%S")) +'.png'
    # screenshot = pyautogui.screenshot(region=region)
    screenshot = pyautogui.screenshot(region=region)

    # Save the screenshot to the media directory
    screenshot_path = os.path.join(settings.MEDIA_ROOT, filename)
    screenshot.save(screenshot_path)

    # Open the screenshot
    image = Image.open(screenshot_path)
    text = pytesseract.image_to_string(image,lang='tur', config='--psm 6')
    print(text)
    context = {
        'lang' : lang,
        'top': top,
        'left': left,
        'width': width,
        "height" : height,
        'text': text,
        'image_url': settings.MEDIA_URL + filename
    }

    # Return the extracted text as a JSON response
    return render(request, 'screenshot.html', context)
