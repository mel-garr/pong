from django.shortcuts import render
from .models import *
from django.http import JsonResponse, HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.



def home(request):
    context = {}
    try :
        user_id = request.session.get('user_id')
        if user_id:
            user = UserL.objects.get(id=user_id)
            context = {'user': user}
        else:
            context = {}
    except:
            context ={}
    
    return render (request, 'home.html', context)

def lobby(request):
    context = {}
    try :
        user_id = request.session.get('user_id')
        if user_id:
            user = UserL.objects.get(id=user_id)
            context = {'user': user}
        else:
            context = {}
    except:
            context ={}
    return render(request, 'game/lobby.html', context)

# @csrf_exempt
def check_login_status(request):
    user_id = request.session.get('user_id')
    if user_id:
        try:
            user = UserL.objects.get(id=user_id)
            status = user.status
            return JsonResponse({'is_logged_in' : True , 'status': user.status})
        except UserL.DoesNotExist:
            return JsonResponse({'is_logged_in' : False})
    else:
        return JsonResponse({'is_logged_in' : False})
    
# @csrf_exempt
def login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            loginId = data.get('LoginId')
            logPass = data.get('password')

            if not loginId or not logPass:
                return JsonResponse({'success': False, 'error': 'give us both login and password'}, status=400)

            user = UserL.objects.get(name=loginId, password=logPass)
            request.session['user_id'] = user.id
            return JsonResponse({'success': True})
        except UserL.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'user/pass does not exist in the db'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Invalid json data'}, status=400)
        except Exception as x :
            return JsonResponse({'success': False, 'error': f'{x}'})
    
    return render(request, '/home.html')

    

# def pick_mode(request):
#     if request.method == 'POST':
#         game_type = request.POST.get('game_type')
#         mode = request.POST.get('mode')

#         request.session['game_type'] = game_type
#         request.session['mode'] = mode

#         return 
    
def offmulti(request):
    return render(request, 'game/offmulti.html')


def setuplobbyoff(request):
    print ('yo')
    if request.method == 'POST':
        data = json.loads(request.body)
        print (data)
