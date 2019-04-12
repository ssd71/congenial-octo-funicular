from django.shortcuts import render
from .models import MessageForm
# Create your views here.

def message_view(request):

    form = MessageForm(request.POST or None)
    if form.is_valid():
        msg = form.save(commit = False)
        msg.by_username = request.user
        msg.save()
        form = MessageForm()

    context = {
        'form':form,
        'next':'',
    }

    return render(request, "messages_u/message_view.html", context)
