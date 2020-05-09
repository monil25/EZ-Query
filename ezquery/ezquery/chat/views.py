from django.shortcuts import render
import speech_recognition as sr
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
# Create your views here.

checkIfRecording = -1


def chatbot(request):

    return render(request, 'chat/chat.html')


@csrf_exempt
def record_audio_start(request):
    global checkIfRecording
    if checkIfRecording == -1:
        checkIfRecording = 1
    main_text = ""
    # obtain audio from the microphone
    while(checkIfRecording == 1):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            r.adjust_for_ambient_noise(source)
            # audio = r.listen(source)
            audio = r.record(source=source, duration=10)
            print("Audio recorded")
        # recognize speech using Google Speech Recognition
        try:
            new_text = r.recognize_google(audio)
            main_text = main_text + "\n" + new_text
            print("Google Speech Recognition thinks you said " + new_text)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(
                "Could not request results from Google Speech Recognition service; {0}".format(e))
        print(main_text)
    return JsonResponse({"text": main_text})


@csrf_exempt
def record_audio_stop(request):
    global checkIfRecording
    checkIfRecording = -1
    return JsonResponse({"text": "Recording stopped"})


@csrf_exempt
def nlp_process(request):
    message = request.POST.get('message', '')
    print(message)
    # do nlp code
    context = {"message": "echo"+message}
    return JsonResponse(context)
