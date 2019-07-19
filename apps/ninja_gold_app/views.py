from django.shortcuts import render, redirect
import random, datetime



def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activity' not in request.session:
        request.session['activity'] = []
    context = {
        'gold': request.session['gold'],
        'activity':request.session['activity']
       
    }
    return render(request, "ninja_gold_app/index.html", context)

def process(request):
    
    if request.POST["building"] == 'farm':
        money = random.randrange(0,20)
        request.session['gold'] += money
        request.session['activity'].append( "<p>Earned "+str(money)+" golds from the "+(request.POST["building"])+"!"+" ("+str(datetime.datetime.now())+")</p>") 
      
    
    if request.POST['building'] == 'cave':
        money = random.randrange(5,10)
        request.session['gold'] += money
        request.session['activity'].append( "<p>Earned "+str(money)+" golds from the "+(request.POST["building"])+"!"+" ("+str(datetime.datetime.now())+")</p>") 

    if request.POST['building'] == 'house':
        money = random.randrange(2,5)
        request.session['gold'] += money
        request.session['activity'].append( "<p>Earned "+str(money)+" golds from the "+(request.POST["building"])+"!"+" ("+str(datetime.datetime.now())+")</p>") 

    if request.POST['building'] == 'casino':
        money = random.randrange(-51,50)
        request.session['gold'] += money
        if money >= 0:
            request.session['activity'].append( "<p>Earned "+str(money)+" golds from the "+(request.POST["building"])+"!"+" ("+str(datetime.datetime.now())+")</p>") 
        else:
            request.session['activity'].append( "<p>Lost "+str(money)+" golds from the "+(request.POST["building"])+"!"+" ("+str(datetime.datetime.now())+")</p>") 

    return redirect('/')

def reset(request):
    request.session['gold'] = 0
    request.session['activity']=[]
    return redirect('/')