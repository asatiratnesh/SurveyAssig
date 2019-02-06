from django import template
register = template.Library()


@register.filter
def in_category(choices, question_id):
    return choices.filter(questions_id=question_id)
