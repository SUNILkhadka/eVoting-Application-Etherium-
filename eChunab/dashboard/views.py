from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Candidate
from . import functions
from django.http import HttpResponse

# Create your views here.

# Global variable


@login_required(login_url="/accounts/login")
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required(login_url="/accounts/login")
def votes(request):
    # res = functions.deployContract()
    candidates = Candidate.objects.all()
    return render(request, 'vote.html',{'candidates': candidates})

# @login_required(login_url="/accounts/submitvote")
def Vote(request,pk):
    # can = Vote.objects.get(pk=pkd)
    Voted_name = Candidate.objects.get(id=pk)
    functions.deployContract(Voted_name)
    return render(request, 'Voted.html')

def Result(request):
    # candidates = Candidate.objects.all()
    # context ={
    #     'candidates': candidates,
    #     'result': result
    # }
    # print(CLASS_INSTANCE)
    print(functions.final_result())
    result = functions.final_result()['result']
    candidates = functions.final_result()['candidates']
    return render(request,'Result.html',{ 'result' : result,'candidates':candidates})
