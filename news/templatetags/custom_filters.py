from news.models import Post
from django import template

register = template.Library()


@register.filter(name='censor')
def censor(text=Post.text):
    if not isinstance(text, str):
        raise ValueError('Можно применить только к строке!')  # Если строка, то в ней уже ищем плохие слова
    if 'редиск' or 'баран' in text:
        text = text.replace('редиск', 'р******')
        text = text.replace('баран', 'б****')
        return text
