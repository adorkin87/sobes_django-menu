from django import template

from ..models import ItemMenu

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    def draw_child(menu, current_item, route, tab_level=4):

        html = ''
        tab = '&nbsp' * tab_level

        if route != -1 and current_item.id in route:
            del route[-1]

        for item in menu.values():
            if item.parent_id == current_item.id:
                html += f'{tab}<a href={item.url}>{item.name}</a><br>'
                if route != -1 and item.id in route:
                    html += draw_child(menu, item, route, tab_level + 4)

        return html

    current_url = context['request'].path[1:]
    menu_html = ''

    menu_items = ItemMenu.objects.filter(menu__name=menu_name).select_related('parent').in_bulk()

    route_active_item = []
    if current_url != '':
        for item in menu_items.values():
            if item.url == current_url:
                route_active_item.append(item.id)
                break
        while menu_items[route_active_item[-1]].parent is not None:
            route_active_item.append(menu_items[route_active_item[-1]].parent_id)

    for item in menu_items.values():
        if item.parent == None:
            menu_html += f'<a href={item.url}>{item.name}</a><br>'
            if item.id in route_active_item:
                menu_html += draw_child(menu_items, item, route_active_item)
            else:
                menu_html += draw_child(menu_items, item, -1)

    return menu_html
