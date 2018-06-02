from django.shortcuts import render
from .models import UserMessage
from accounts.models import *
from warhawks.models import *

# Create your views here.

def message_home(request):
    if request.user.is_authenticated:
        # get message
        unread = UserMessage.objects.filter(m_to=request.user, seen=False)
        read   = UserMessage.objects.filter(m_to=request.user, seen=True)
        
        context = {
            'unread': unread,
            'read': read
        }
        return render(request, 'messenger/messages.html', context)
    else:
        return redirect("accounts:home")