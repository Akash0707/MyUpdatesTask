from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from rest_framework.views  import APIView
from django.core.mail import send_mail,EmailMessage
from emailproject import settings

@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(APIView):
 
 def post(self, request, *args, **kwargs):
    content1=Student.objects.all().last()
    json_data = request.body
    stream = io.BytesIO(json_data)
    pythondata = JSONParser().parse(stream)
    serializer = StudentSerializer(data = pythondata)
    if serializer.is_valid():
        serializer.save()
        
        print(content1)
        
        email1 = pythondata['email']
        message = "Hello  "
        subject = "The mail send through the API"
        from_email = "
        to_email = email1
        send_mail(subject, message, from_email, (email1,),
                    auth_password=settings.EMAIL_HOST_PASSWORD)
        print(email1)
        res = {'msg': 'Data Created'}
        json_data = JSONRenderer().render(res)
        
        return HttpResponse(json_data, content_type='application/json')
    json_data = JSONRenderer().render(serializer.errors)
    return HttpResponse(json_data, content_type='application/json')

    
