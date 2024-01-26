from django.shortcuts import render
from .models import *
from .serializer import roleSerializer
from .serializer import pollingSerializer
from django.http import JsonResponse,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET','POST'])
def getroles(request):
	if request.method == 'GET':
		roles_list = roles.objects.all()
		ser_data = roleSerializer(roles_list,many=True)
		return JsonResponse(ser_data.data,safe=False)
	elif request.method == 'POST':
		ser = roleSerializer(data = request.data)
		if ser.is_valid():
			ser.save()
			return Response(ser.data)
		else:
			return HttpResponse("Error While Saving Data")

@api_view(['GET','POST'])
def putpoll(request):
	if request.method =='GET':
		poll_list = polling.objects.all()
		dataa = pollingSerializer(poll_list,many=True)
		return JsonResponse(dataa.data,safe=False)
	elif request.method == 'POST':
		ser = pollingSerializer(data = request.data)
		if ser.is_valid():
			ser.save()
			return Response(ser.data)
		else:
			return HttpResponse("error Occurred")
