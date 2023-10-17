from django import template

from menu.models import MenuItem


register = template.Library()


@register.simple_tag
def draw_menu(menu_name, parent_item=None):
    menu_items = MenuItem.objects.filter(
        name=menu_name, parent=parent_item).select_related('parent')

    if not menu_items:
        return ""

    menu_html = "<ul>"
    for item in menu_items:
        menu_html += f"<li><a href='{item.url}'>{item.title}</a>"
        menu_html += draw_menu(menu_name, item)
        menu_html += "</li>"

    menu_html += "</ul>"
    return menu_html
