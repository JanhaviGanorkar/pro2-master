from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from django.utils.timezone import now

@login_required
def chat_room(request):
    if request.method == "POST":
        message = request.POST.get('message')
        if message:
            Message.objects.create(user=request.user, content=message, timestamp=now())
        return redirect('chat_room')  # Page reload hoke naya message dikhega
    messages = Message.objects.order_by('timestamp')[:50]  # Oldest messages first

    # messages = Message.objects.order_by('-timestamp')[:50]  # Last 50 messages dikhayenge
    return render(request, 'chat/chat_room.html', {'messages': messages})
