from django import template
from blog.models import Category

register = template.Library()


@register.inclusion_tag('blog/include/tags/top_menu.html')
def get_categories():
    category = Category.objects.filter(parent__isnull=True).order_by('name')
    return {"list_category": category}


@register.inclusion_tag('blog/include/tags/recipes_tag.html')
def get_last_posts():
    posts = Post.objects.select_related("category").order_by("-id")[:5]
    return {"list_last_post": posts}
