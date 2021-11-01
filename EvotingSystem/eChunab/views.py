from django.shortcuts import render
from django.http import HttpResponse
from . import functions


def home(request):
	return render(request,"eChunab/base.html")

def vote(request):
	return HttpResponse("<h1> Hello mf are you here for vote </h1>")


def votingPage(request):
	# res = functions.deployContract()
	res = functions.account()

	item = [
		res
	]
	for i in range(len(item)):
		print(item[i])
	context = {
		'item': item
	}
	return render(request,'eChunab/base.html', res )


