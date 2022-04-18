from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import Neighborhood,Business
from .forms import NewNeighborhoodForm,NewBusinessForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    neighborhoods = Neighborhood.objects.all()
    

    return render(request, 'index.html',{"hoods":neighborhoods})

@login_required(login_url='/accounts/login/')
def profile(request):

    return render(request, 'profile.html')

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



