from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.form_to_upload, name =  'form'),
    path('uploaded', views.upload_file, name = 'uploaded'),
    path('file_lists', views.files_directory, name = 'file_lists'),
    path ('dataframe/<str:file>', views.dataframe_view, name = 'dataframe_view'),
    path('file_deleted/<str:file>', views.delete_file, name = 'file_deleted'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
