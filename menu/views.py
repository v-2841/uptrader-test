from django.shortcuts import render

from menu.models import MenuItem


def home(request):
    main_menu_items = MenuItem.objects.filter(name='main_menu', parent=None)
    print(main_menu_items)
    return render(request, 'menu/home.html',
                  {'main_menu_items': main_menu_items})
