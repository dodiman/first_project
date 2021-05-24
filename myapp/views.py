from django.shortcuts import render

# Create your views here.
def myindex(request):
	context = {}
	return render(request, 'myindex.html', context)
