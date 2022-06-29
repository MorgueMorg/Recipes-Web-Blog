from django import template
from blog.models import Category, Post

register = template.Library()


def get_all_categories():
    return Category.objects.all()


@register.simple_tag()
def get_list_category():
    """Вывод всех категорий"""
    return get_all_categories()


@register.inclusion_tag('blog/include/tags/top_menu.html')
def get_categories():
    category = Category.objects.all()
    # category = get_all_categories()
    return {"list_category": category}

