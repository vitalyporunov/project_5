from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import MessageForm

# ✅ Inbox - Displays received messages (excluding archived ones)
@login_required
def inbox(request):
    messages = Message.objects.filter(recipient=request.user, is_archived=False).order_by('-timestamp')
    return render(request, 'messaging/inbox.html', {'messages': messages})

# ✅ Message Detail - Marks message as read when viewed
@login_required
def message_detail(request, pk):
    message = get_object_or_404(Message, pk=pk, recipient=request.user)
    
    if not message.is_read:
        message.is_read = True
        message.save()
    
    return render(request, 'messaging/message_detail.html', {'message': message})

# ✅ Send Message - Allows users to send messages
@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user  # ✅ Assign sender
            message.save()
            return redirect('inbox')  # ✅ Redirect back to inbox after sending
    else:
        form = MessageForm()

    return render(request, 'messaging/send_message.html', {'form': form})

# ✅ Archive Message - Moves messages to archived
@login_required
def archive_message(request, pk):
    message = get_object_or_404(Message, pk=pk, recipient=request.user)  # ✅ Restrict archiving to recipient only
    message.is_archived = True
    message.save()
    return redirect('inbox')

# ✅ Archived Messages - Displays all archived messages
@login_required
def archived_messages(request):
    messages = Message.objects.filter(recipient=request.user, is_archived=True).order_by('-timestamp')
    return render(request, 'messaging/archived_messages.html', {'messages': messages})
