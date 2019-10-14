from django.forms.formsets import formset_factory
from django.forms import ModelForm, inlineformset_factory

from .models import Question, Choice


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ('question_text',)

class ChoiceForm(ModelForm):
    class Meta:
        model = Choice
        fields = ('choice_text',)

ChoiceFormSet = formset_factory(ChoiceForm, extra=0,
                                min_num=3, validate_min=True)
