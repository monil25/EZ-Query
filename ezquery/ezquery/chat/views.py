from django.shortcuts import render
import speech_recognition as sr
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def chatbot(request):
    return render(request, 'chat/chat.html')


@csrf_exempt
def audio_to_text(request):
    audio = request.POST.get('audio', '')
    print(audio)
    # r = sr.Recognizer()
    # with sr.AudioFile(audio) as source:
    #     r.adjust_for_ambient_noise(source)

    #     print("Converting Audio To Text ..... ")

    #     audio = r.listen(source)
    # try:
    #     text = r.recognize_google(audio, language='hi-IN')
    #     print("Converted Audio Is :")
    return JsonResponse({"text": audio})
    # except Exception as e:
    #     print("Error {} : ".format(e))
