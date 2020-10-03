from django.shortcuts import render
from csv_file.models import Profile

# Create your views here.

import csv,io
from django.contrib import messages
from subprocess import run,PIPE
import sys

def index(request):
   template = "index.html"
   if request.method == "GET":
      return render(request, template)
def external(request):
   template  = "home.html"
   if request.method == "GET":
      return render(request, template)
   data2 = Profile.objects.all()
   
   content = request.POST.get('content_email')
   
   import smtplib
   import pandas as pd

   import ssl
   from email.mime.text import MIMEText
   from email.utils import formataddr
   from email.mime.multipart import MIMEMultipart
   from email.mime.base import MIMEBase
   from email import encoders


   sender_email = request.POST.get('r_email')  #Add your email
   sender_name = request.POST.get('r_name')
   password = request.POST.get('r_password')   #Add your password
   final = 'Email sent!'

   for data in data2:

    print("Sending to " + data.name)
    msg = MIMEMultipart()
    msg['Subject'] = request.POST.get('subject_email')
    msg['From'] = formataddr((sender_name, sender_email))
    msg['To'] = formataddr((data.name, data.email))

    msg.attach(MIMEText("""<h2>Hello, """ + data.name +"""</h2><p>"""+ content +"""</p>"""  , 'html'))


    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        context = ssl.create_default_context()
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, data.email, msg.as_string())
        print(final)
    except Exception as e:
        print(f'Oh no! Something bad happened!n{e}')
        continue
        
    finally:
        # print('Closing the server...')
        server.quit()

   return render(request, template,{'data1':final})














def csv_upload(request):

   

   template  = "csv_upload.html" 
   code = request.POST.get('code')
   submit = request.POST.get('submit')
   #data = Profile.objects.all()
   prompt = {
      'order': 'Column headings case and order in the CSV should be [name], [email]'
   } 
   if request.method == "GET":
      return render(request, template,prompt)
      if submit:
        if code == '1234' :
         
         return render(request, template,prompt)

         csv_files = request.FILES['file']

         if not csv_files.name.endswith('.csv'):
             messages.error(request, 'This is not a csv file')  
         data_set = csv_files.read().decode('UTF-8')
         io_string = io.StringIO(data_set)
         next(io_string)
         for column in csv.reader(io_string, delimiter=',',quotechar="|"):
            _, created = Profile.objects.update_or_create(
              name = column[0],
              email = column[1],

          )
         context = {}
         return render(request,template,{'data':'File Uploaded'})
      else:
         return render(request, template, {'data':'code is not valid!'})