from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from drug import models
from django.views import generic
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from user.forms import SignUpForm
from django.contrib.auth.decorators import login_required


# @login_required
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('signup')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


# def index(request):
#     molecule = models.Molecule.objects.order_by('id')
#     return render(request, 'user/index.html', {'molecule': molecule})
#     # out = ', '.join([q.MoleculeName for q in last_product])
#     # return HttpResponse(out)

class index(generic.ListView):
    template_name = 'user/index.html'
    context_object_name = 'molecule'

    def get_queryset(self):
        return models.Molecule.objects.order_by('id')


# def detail(request, drug_id):
#     molecule = get_object_or_404(models.Molecule, pk=drug_id)
#     return render(request, 'user/detail.html', {'molecule': molecule})

class detail(generic.DetailView):
    model = models.Molecule
    template_name = 'user/detail.html'


# def detai(request, generic_id):
#     generic = get_object_or_404(models.Generic, pk=generic_id)
#     return render(request, 'user/detai.html', {'generic': generic})

class detai(generic.DetailView):
    model = models.Generic
    template_name = 'user/detai.html'
