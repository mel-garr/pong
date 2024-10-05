from django.shortcuts import render

# Create your views here.
def room(request, room_id):
    return render(request, 'test/room.html', {'room_id': room_id})

def index(request):
    return render(request, "test/index.html")

