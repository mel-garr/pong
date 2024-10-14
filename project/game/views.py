from .models import *
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render, get_object_or_404
from .game_objects.pgame import *

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


def setuplobbyoff(request):
    if request.method == 'POST':
        try :
            data = json.loads(request.body)
            valid_keys = ['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight', 'Space'] + list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
            # print (data)
            required_fields = ['p1nickname', 'p1paddle', 'p1ball', 'p1field', 
                            'p2nickname', 'p2paddle', 'p2ball', 'p2field',
                            'keyupp1', 'keydownp1',
                            'keyupp2', 'keydownp2']

            seen = set()

            if not all(data.get(field) for  field in required_fields):
                return JsonResponse({'status': 'missing fields'}, status=400)

            keys_field = ['keyupp1', 'keydownp1',
                        'keyupp2', 'keydownp2']

            for field in keys_field:
                if data[field] not in valid_keys:
                    return JsonResponse({'status': 'Invalid key provided'}, status=400)
                if data[field] in seen:
                    return JsonResponse({'status': 'duplicate key provided'}, status=400)
                seen.add(data[field])

            P1 = playerData(
                
                name = data['p1nickname'],
                paddle = data['p1paddle'],
                ball = data['p1ball'],
                field = data['p1field'],
                keys = {
                    'keyup' : data['keyupp1'], 
                    'keydown': data['keydownp1'],
                    }
            )
            P2 = playerData(
                name = data['p2nickname'],
                paddle = data['p2paddle'],
                ball = data['p2ball'],
                field = data['p2field'],
                keys = {
                    'keyup' : data['keyupp2'].lower(), 
                    'keydown': data['keydownp2'].lower(),
                    }
            )
            P1.save()
            P2.save()
            party = roomData(
                name = 'Defi',
                gametype = 'Challenge',
                gamestatus = 'pause',
            )
            party.save()
            party.redteamplayers.add(P1)
            party.blueteamplayers.add(P2)
            party.save()
            # print (party.id)
            return JsonResponse({'status' : 'Lobby created ok', 'room_id': party.id}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'status' : 'invlaid JSON'}, status=400)
        except Exception as e :
            return JsonResponse({'status':'error', 'message':str(e)}, status=500)
    return JsonResponse({'status': 'not ok'}, status=405)
            
def offmulti_view(request, room_id):
    try :
        room = get_object_or_404(roomData, id=room_id)
        P1 = room.redteamplayers.first()
        P2 = room.blueteamplayers.first()

        
    except Exception as e :
        return JsonResponse({'status':'errro', 'message':str(e)}, status=500)

    return render(request, 'game/offmulti.html', {'room_id' : room_id, 'P1' : P1, 'P2' : P2})



def lobbyon(request):
    context = {}
    try :
        user_id = request.session.get('user_id')
        print(user_id)
        if user_id:
            user = UserL.objects.get(id=user_id)
            context = {'user': user}
        else:
            context = {}
    except:
            context ={}
    return render(request, 'game/lobbyon.html', context)

