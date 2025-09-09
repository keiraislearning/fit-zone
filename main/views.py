from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406423282',
        'name': 'Keira Nuzahra Anjani',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)