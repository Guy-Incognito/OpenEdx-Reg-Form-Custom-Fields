from django.forms import ModelForm

from .models import ExtraInfo


class ExtraInfoForm(ModelForm):
    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """

    def __init__(self, *args, **kwargs):
        super(ExtraInfoForm, self).__init__(*args, **kwargs)
        self.fields['country'].required = True

    class Meta(object):
        model = ExtraInfo
        fields = ('country',)
