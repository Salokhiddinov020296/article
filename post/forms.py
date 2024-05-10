from django import forms

from post.models import AclassModel


class ClassModelAdmin(forms.ModelForm):
    # article_uz = forms.TextField(required=False)
    # article_en = forms.Textarea(required=False)
    # article_ru = forms.Textarea(required=False)
    # annotation_uz = forms.Textarea(required=False)
    # annotation_en = forms.Textarea(required=False)
    # annotation_ru = forms.Textarea(required=False)
    # key_word_ru = forms.Textarea(required=False)
    # key_word_en = forms.Textarea(required=False)
    # key_word_uz = forms.Textarea(required=False)

    class Meta:
        model = AclassModel
        fields = '__all__'