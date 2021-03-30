from django.shortcuts import render

def index(request):
    """The home page for My Learnings."""
    return render(request, 'my_learning/index.html')