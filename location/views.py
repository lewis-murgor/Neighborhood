from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import Neighborhood,Business, Post,Profile
from .forms import NewNeighborhoodForm,NewBusinessForm,PostForm,UpdateProfileForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    neighborhoods = Neighborhood.objects.all()
    

    return render(request, 'index.html',{"hoods":neighborhoods})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    neighborhood = Neighborhood.objects.filter(user = current_user)
    profile = Profile.objects.filter(user_id = current_user)


    return render(request, 'profile.html',{"hoods":neighborhood, "profile":profile})

@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('profile')
    else:
        form = UpdateProfileForm()
    return render(request, 'update_profile.html', {"form": form})

@login_required(login_url='/accounts/login/')
def create_neighborhood(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewNeighborhoodForm(request.POST)
        if form.is_valid():
            neighborhood = form.save(commit=False)
            neighborhood.user = current_user
            neighborhood.save()
        return redirect('index')

    else:
        form = NewNeighborhoodForm()
    return render(request, 'create_neighborhood.html', {"form": form})

@login_required(login_url='/accounts/login/')
def neighborhood(request,neighborhood_id):
    current_user = request.user
    neighborhood = Neighborhood.objects.get(id = neighborhood_id)
    business = Business.objects.filter(neighborhood=neighborhood_id)
    if request.method == 'POST':
        form = NewBusinessForm(request.POST)
        if form.is_valid():
            business = form.save(commit=False)
            business.user = current_user
            business.save()
            return redirect('neighborhood')

    else:
        form = NewBusinessForm()
    return render(request, 'create_business.html', {"form": form,"business":business,"neighborhood":neighborhood})

@login_required(login_url='/accounts/login/')
def create_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('post')

    else:
        form = PostForm()

    return render(request, 'create_post.html', {"form": form})

@login_required(login_url='/accounts/login/')
def post(request):
    post=Post.objects.all()

    return render(request, 'post.html',{"posts": post})

@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'business' in request.GET and request.GET["business"]:
        name = request.GET.get("business")
        searched_business = Business.search_by_name(name)
        message = f"{name}"

        return render(request, 'search.html',{"message":message,"business": searched_business})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def join(request):
    current_user = request.user
    if request.method == "POST":
        neighborhood_id = request.POST.get('neighborhood_id')
        neighborhood = Neighborhood.objects.get(id=neighborhood_id)

        if current_user in neighborhood.joins.all():
            neighborhood.joins.remove(current_user)
        else:
            neighborhood.joins.add(current_user)
    return redirect('index')




