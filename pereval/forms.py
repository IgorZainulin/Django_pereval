from django import forms
from django.core.exceptions import ValidationError

from .models import *

from datetime import date

class PostForm(forms.ModelForm):
    class Meta:
        model = Pereval
        fields = [
            '',
            '',
            '',
            '',

        ]
    #
    # def clean_text(self):
    #     cleaned_data = super().clean()
    #     text = cleaned_data.get("text")
    #     if text is not None and len(text) < 20:
    #         raise ValidationError({
    #             "text": "Текст не может быть менее 20 символов."
    #         })
    #
    #     return text


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = [
#             'comm_text',
#         ]













    # def clean(self):
    #     cleaned_data = super().clean()
    #     author = cleaned_data['author']
    #     today = date.today()
    #     post_limit = Post.objects.filter(author=author, create_time__date=today).count()
    #     if post_limit >= 3:
    #         raise ValidationError('Нельзя публиковать больше трех постов в сутки!!!')
    #     return cleaned_data







