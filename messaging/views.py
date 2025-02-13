from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import MessageForm

@login_required
def inbox(request):
    messages = Message.objects.filter(recipient=request.user, is_archived=False)
    return render(request, 'messaging/inbox.html', {'messages': messages})

@login_required
def message_detail(request, pk):
    message = get_object_or_404(Message, pk=pk, recipient=request.user)
    message.is_read = True  # ✅ Mark as read
    message.save()
    return render(request, 'messaging/message_detail.html', {'message': message})

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            
            # ✅ Ensure recipient is set
            if 'recipient' in form.cleaned_data:
                message.recipient = form.cleaned_data['recipient']
            else:
                return redirect('send_message')  # Handle missing recipient

            message.save()
            return redirect('inbox')
    else:
        form = MessageForm()
    return render(request, 'messaging/send_message.html', {'form': form})

@login_required
def archive_message(request, pk):
    message = get_object_or_404(Message, pk=pk, recipient=request.user)  # ✅ Restrict access
    message.is_archived = True
    message.save()
    return redirect('inbox')
