from django.http import HttpResponse,HttpResponseNotFound
from django.shortcuts import render,get_object_or_404 ,redirect
from .models import Note
from .forms import NoteForm
from django.views.decorators.http import require_POST

def home(request):
    return HttpResponse("Welcome Home")

# data = [
#     {'name': 'note1', 'content': 'This is my first note'},
#     {'name': 'note2', 'content': 'This is my second note'},
#     {'name': 'note3', 'content': 'This is my third note'},
# ]


def notes(request):
    data = Note.objects.all()
    return render(request, 'quicknotes/index.html', {'notes': data, 'form': NoteForm()})



def note(request, note_id):
    data = get_object_or_404(Note, pk=note_id)

    # data = Note.objects.filter(pk=note_id)
    # print(data)
    # if data == None or str(data) == '<QuerySet []>':
    #     return HttpResponseNotFound("<h1>Page not found</h1>")
    # if data !=None:
    note_form = NoteForm(instance=data)
    return render(request, 'quicknotes/notes.html', {'note': data,"form":note_form})        

# @require_POST
def add(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('notes')
    return HttpResponse(status=405)



def edit(request,note_id):
        note_data = get_object_or_404(Note, pk=note_id)

        form = NoteForm(request.POST, instance=note_data)
        if form.is_valid():
            form.save()
        return redirect('note', note_id=note_data.id)
        return HttpResponse(status=405)

def deleteform(request,note_id):
    note_data = get_object_or_404(Note, pk=note_id)
    if request.method == "POST":
        note_data.delete()
        return redirect('notes')

