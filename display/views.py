from django.shortcuts import render, redirect

# Create your views here.
from .form import ContactForm
from .models import Profile
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages

def home(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            body ={
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, body['email'], ['prajapati143a@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request,"Success....Your message has been sent to Avinash!!")
            return redirect('home')
        messages.error(request, "message not sent.")
 
    else:
        form  = ContactForm()
    return render(request, 'home.html',{'form': form})
