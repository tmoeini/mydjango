from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpRequest
from django.views.decorators.csrf import csrf_exempt
import json
from web.models import Expense,Income,Token,User
from datetime import datetime

# Create your views here.
@csrf_exempt 
def submit_expense(request):
   this_token=request.POST['token']
   # print (this_token)
   this_user=User.objects.filter(token__token=this_token).get()
   if 'date' not in request.POST:
    now=datetime.now()
   Expense.objects.create(user=this_user,amount=request.POST['amount'],text=request.POST['text'],date=now)
   return JsonResponse({'status':'ok',},encoder=json.JSONEncoder)
@csrf_exempt 
def submit_income(request):
   this_token=request.POST['token']
   this_user=User.objects.filter(token__token=this_token).get()
   if 'date' not in request.POST:
    now=datetime.now()
   Income.objects.create(user=this_user,amount=request.POST['amount'],text=request.POST['text'],date=now)
   return JsonResponse({'status':'ok',},encoder=json.JSONEncoder)   

   
   
