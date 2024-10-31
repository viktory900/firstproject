from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    if request.method == 'POST':
        genre = request.POST.get('genre')
        if genre == 'comedy':
            return redirect('comedy')
        elif genre == 'drama':
            return redirect('drama')
        elif genre == 'horror':
            return redirect('horror')
    return render(request, 'main/index.html')

def comedy(request):
    if request.method == 'POST':
        genre = request.POST.get('genre')
        if genre == 'comedy':
            return redirect('comedy')
        elif genre == 'drama':
            return redirect('drama')
        elif genre == 'horror':
            return redirect('horror')
    return render(request, 'main/comedy.html')

def drama(request):
    if request.method == 'POST':
        genre = request.POST.get('genre')
        if genre == 'comedy':
            return redirect('comedy')
        elif genre == 'drama':
            return redirect('drama')
        elif genre == 'horror':
            return redirect('horror')
    return render(request, 'main/drama.html')

def horror(request):
    if request.method == 'POST':
        genre = request.POST.get('genre')
        if genre == 'comedy':
            return redirect('comedy')
        elif genre == 'drama':
            return redirect('drama')
        elif genre == 'horror':
            return redirect('horror')
    return render(request, 'main/horror.html')


def main_page(request):
    theme = request.COOKIES.get('theme', 'light')  # По умолчанию 'light' если куки не установлены
    # Передаем тему в шаблон
    return render(request, 'main/index.html', {'theme': theme})

def toggle_theme(request):
    # Переключаем тему
    if request.method == 'POST':
        current_theme = request.COOKIES.get('theme', 'light')
        if current_theme == 'light':
            new_theme = 'dark'
        else:
            new_theme = 'light'
        # Устанавливаем новую тему в куки
        response = redirect('main_page')  # Переход к основной странице
        response.set_cookie('theme', new_theme, max_age=3600)  # Сохраняем куки на час
        return response
    return redirect('main_page')

