from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from .form import User_Form
from django.contrib.auth.models import User
from django.core.mail import send_mail
from urlgenerate import settings
# Create your views here.
def register(request):
    form=User_Form()
    if request.method=="POST":
        form=User_Form(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            form.save()
            url=request.build_absolute_uri(form.get_absloute_url())
            subject=' {} succssfully saved'.format(cd['username'])
            message='login here {}'.format(url)
            send_mail(subject,message,settings.EMAIL_HOST_USER,[cd['email']])
            form=User_Form()
            return render(request,'register.html',{'form':form,'message':'saved done and also email sent'})
        else:
            form=User_Form()
            return render(request,'register.html',{'form':form,'message':'method is not post'})
    else:
        return render(request, 'register.html', {'form':form,'message': 'method is not post'})

    return None