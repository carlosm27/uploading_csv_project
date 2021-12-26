from django.shortcuts import render, redirect, Http404

from django.core.files.base import ContentFile
from os import listdir
from os.path import isfile, join
import os
from django.core.files.uploadedfile import UploadedFile

from django.conf import settings
from django.core.files.storage import FileSystemStorage, default_storage
from .models import Document

from .form import DocumentForm
import pandas as pd

def upload_file(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        file_storage = FileSystemStorage()
        filename = file_storage.save(myfile.name, myfile)
        uploaded_file_url = file_storage.url(filename)
        context = {
            'uploaded_file_url' : uploaded_file_url,
        }
        return render(request,'upload_csv/uploaded.html', context)
    return render (request, 'upload_csv/uploaded.html')

def form_to_upload(request):
    if request.method =='POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_lists')
    else:
        form = DocumentForm()
    context = {
        'form' : form,
    }
    return render(request,'upload_csv/csv_form.html', context)

def files_directory(request):
    context_dict = {}
    files = os.listdir(os.path.join(settings.MEDIA_ROOT,"documents"))
    context_dict['files'] = files
    context = context_dict
    return render(request, 'upload_csv/file_lists.html', context )



def dataframe_view(request, file):
    files_path = 'media/documents/'

    files = file
    read_data = pd.read_csv(files_path +  files)
    df = pd.DataFrame(read_data)
    context = { 'df' : df.to_html()}
    return render(request, 'upload_csv/dataframe.html', context)

def delete_file(request, file):
    files_path = 'media/documents/'
    files = file
    if request.method == 'POST':
        data_file = files_path + files
        os.remove(data_file)
        return redirect('upload_csv/file_lists.html')
    return render(request, 'upload_csv/file_lists.html')



