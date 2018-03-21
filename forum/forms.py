from django.forms import ModelForm

from .models import Forum


class ForumUpdateForm(ModelForm):
    class Meta:
        model = Forum
        fields = ('moderators',)
