from django.shortcuts import render
import csv,io
from django.contrib import messages
from subprocess import run,PIPE
import sys
def button(request):
   return render(request, 'home.html')
# def external(request):
  
#    name = request.POST.get('r_name')
#    email = request.POST.get('r_email')
#    subject = request.POST.get('subject_email')
#    content = request.POST.get('content_email')
#    out = run([sys.executable,'E:\\django_email_project\\link_mail.py',name,email,subject,content],shell=False,stdout=PIPE)
#    print(out)
   
#    return render(request, 'home.html',{'data1':out.stdout})

