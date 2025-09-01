from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request, param=None):
    if param:
        return HttpResponse(
            f"""
            <h1>Hello Django!</h1>
            <p>Bonjour, {param}</p>
            """
        )
    else:
        return HttpResponse("<h1>Hello Django!</h1>")

def contact(request):
    return HttpResponse(
        """
        <h1>Page Contact</h1>
        <p>Ceci est une page de contact !!</p>
        """
    )

def about(request):
    return HttpResponse(
        """
        <h1>Page A propos</h1>
        <p>Ceci est une page A propos !!</p>
        """
    )


