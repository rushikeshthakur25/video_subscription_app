from django.shortcuts import render,redirect
from . models import  MovieUp
from . models import  UserSubscription
from . forms import SignUpForm
from django.contrib.auth import login
# from .forms import User
from .models import Price
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render (request ,'sub/index.html')

def signup(request):
    if request.method =='POST':
        form = SignUpForm(request.POST) 

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('index')
    else:
        form = SignUpForm()

    return render(request, 'sub/signup.html',{'form':form}) 

# @login_required(login_url='/login/')
def upmovie(request):
    if request.method == 'POST':
        mname = request.POST['mname']
        mlanguage = request.POST['mlanguage']
        mdescription = request.POST['mdescription']
        mpic = request.FILES['mpic']
        mvideo = request.FILES['mvideo']


        newuser = MovieUp.objects.create(mname=mname,mlanguage=mlanguage,mdescription=mdescription,mpic=mpic,mvideo=mvideo)

        # return redirect('list')
    return render(request,'sub/upmovie.html' )

@login_required
def list(request):
    data = MovieUp.objects.all()
    
    if user_has_active_subscription(request.user):
                return render(request,'sub/movie_list.html',{'data':data})
        # return render(request,'sub/movie_list.html',{'data':data})
    else:
        return render(request,'sub/fail.html')
                # return render(request,'sub/fail.html',{'plan': plan})    
    # return render(request,'sub/login.html')

def display_movie(request):
    data = MovieUp.objects.all()
    return render(request,'sub/display.html',{'data':data})

@login_required
def price(request):
    plans = Price.objects.all()
    return render(request, 'sub/price.html', {'plans': plans})    

# @login_required
# def subscription_plans(request):
#     return render(request ,'sub/price.html')
    
@login_required
def subscribe(request, plan_id):
    plan = Price.objects.get(pk=plan_id)
    payment_successful = True
    
    if payment_successful:
        UserSubscription.objects.create(user=request.user, plan=plan)
        return render(request, 'sub/success.html', {'plan': plan})
    else:
        return render(request, 'sub/failure.html', {'plan': plan})


# def watch_video(request, video_id):
#     video = get_object_or_404(Video, id=video_id)
#     return render(request, 'sub/list.html', {'video': video})

def user_has_active_subscription(user):
    return UserSubscription.objects.filter(
        user=user,
        # expiry_date__gt=timezone.now()  # Check if the subscription is still active
    ).exists()

# def profile(request):
#     user_subscription = UserSubscription.objects.filter(user=request.user).first()

#     if user_subscription and user_subscription.has_active_subscription():
#         remaining_days = user_subscription.calculate_remaining_days()
#         return render(request, 'sub/profile.html', {'remaining_days': remaining_days})
#     else:
#         return redirect('subscription-plans')