class DeleteFile(DeleteView):
    model = Document
    files = os.listdir(os.path.join(settings.MEDIA_ROOT, "documents"))
    context_object_name = 'files'
    success_url = reverse_lazy('files')

def csv_dataframe(request):
    files_path = 'media/documents'

    context = {}
    for files in os.listdir(files_path):
        if 'name' in request.GET:
            file = request.GET['name']
            if file == files:
                read_data = pd.read_csv(files_path % file)
                df = pd.DataFrame(read_data)
                context = {
                    'df' : df.to_html(),
                }
        return render(request, 'upload_csv/dataframe.html', context)
    return render(request, 'upload_csv/dataframe.html', context)


def delete_file(request):
    path = default_storage.save('media/documents/', ContentFile(b'Athletic_Shoes.csv'))

    if request.method == 'POST':
        default_storage.delete(path)
        return redirect('/')

    context = {'default_storage': default_storage}
    return render(request, 'upload_csv/file_lists.html', context)

def csv_dataframe(request):
    files_path = 'media/documents/'

    context = {}

    for file in os.listdir(files_path):
        read_data = pd.read_csv(files_path + file)
        df = pd.DataFrame(read_data)

        context = {'df' : df.to_html()}
    return render(request, 'upload_csv/dataframe.html', context)
