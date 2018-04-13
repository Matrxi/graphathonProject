from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from mysite.core.forms import SignUpForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from mysite.core.models import Document
from mysite.core.forms import DocumentForm
from django.core.urlresolvers import reverse
from django.core.cache import cache
from django.shortcuts import get_object_or_404
import cgi
import json
import urllib.request, urllib.parse, urllib.error


@login_required
def home(request):
    return redirect('homewelcome')

@login_required
def homewelcome(request):
    return render(request, 'home.html')


def contact(request):
    return render(request, 'contact.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'core/upload_success.html')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })

def uploaded_files(request):
    if request.user.is_authenticated():
       documents = Document.objects.all()
       return render(request, 'core/all_files.html', { 'documents': documents })
    #return render(request, 'core/all_files.html')

def delete_first_file(request):
    if request.method != 'POST':
        raise HTTP404
    else:
        documents = Document.objects.all()
        for obj in documents:
            obj.delete()
            break
    return uploaded_files(request)

def delete_all_files(request):
    if request.method != 'POST':
        raise HTTP404
    else:
        documents = Document.objects.all()
        for obj in documents:
            obj.delete()
    return uploaded_files(request)
