from django.contrib import admin

# Register your models here.
def start_game(request):
    
    return render(request, "start.html")