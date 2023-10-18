from django import template
from django.utils.html import format_html

from menu.models import MenuItem


register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    current_url = context['request'].path
    menu_items = MenuItem.objects.all()
    if not menu_items:
        return ''

    current_item = None
    current_items = menu_items.filter(url=current_url)
    for item in current_items:
        i_item = item
        while i_item.parent:
            i_item = menu_items.get(id=i_item.id).parent
        if menu_name == i_item.name:
            current_item = item
            break

    menu_html = ''
    if menu_items.filter(parent=current_item):
        menu_html += '<ul>'
        for children in menu_items.filter(parent=current_item):
            menu_html += (f"<li><a href='{children.url}'>"
                          + f"{children.title}</a></li>")
        menu_html += '</ul>'

    while menu_items.get(id=current_item.id).parent:
        temp_html = '<ul>'
        for children in menu_items.filter(parent=current_item.parent):
            if children == current_item:
                temp_html += (f"<li><a class='selected' href='{children.url}'>"
                              + f"{children.title}</a></li>")
                temp_html += menu_html
            else:
                temp_html += (f"<li><a href='{children.url}'>"
                              + f"{children.title}</a></li>")
        temp_html += '</ul>'
        menu_html = temp_html
        current_item = menu_items.get(id=current_item.parent.id)
    menu_html = ('<ul>' + f"<li><a class='selected' href='{current_item.url}'>"
                 + f"{current_item.title}</a></li>" + menu_html + '</ul>')
    return format_html(menu_html)
