from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from dashboard.models import Candidate
# from django.contrib.auth.models import User
# from accounts.forms import UserForm
from .forms import AddCandidate

# Create your views here.
def officer(request):
    can_data = Candidate.objects.all()
    # user_data = User.objects.all()
    # print(can_data)
    return render(request, 'officer.html', {'candata':can_data})

def add_candidate(request):
    fm = AddCandidate(request.POST)
    if fm.is_valid():
        fm.save()
        return redirect('/officer')
    else:
        return render(request, 'add-candidate.html', {'form':fm})

def delete_candidate(request):
    data = request.POST
    id = data.get('id')
    canddata = Candidate.objects.get(id=id)
    canddata.delete()
    return redirect('/officer')

# def edit_candidate(request, id):
#     cand = Candidate.objects.get(id=id)
#     fm = AddCandidate(request.POST)
#     return render(request, 'edit-candidate.html', {'form':fm})
#     if fm.is_valid():
#         fm.save()
#         return redirect('/officer')

def edit_candidate(request, id):
    context ={}
    obj = get_object_or_404(Candidate, id = id)
    form = AddCandidate(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        return redirect('/officer')

    context["form"] = form
 
    return render(request, "edit-candidate.html", context)
