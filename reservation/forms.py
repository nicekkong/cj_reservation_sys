from django import forms
# from django.forms import widgets
from django.contrib.admin import widgets

from .models import ConferenceInfo, UserInfo



# FAVORITE_COLORS_CHOICES = (
#     ('blue', 'Blue'),
#     ('green', 'Green'),
#     ('black', 'Black'),
# )

ATTENDANCE_CHOICES = ((user.id, user.name, ) for user in UserInfo.objects.all())


class ConferenceSaveForm(forms.ModelForm):
    attendance = forms.MultipleChoiceField(label='참석자',
                    required=False,
                    widget=forms.CheckboxSelectMultiple,
                    choices=ATTENDANCE_CHOICES,
    )
    start_date = forms.SplitDateTimeWidget()

    class Meta:
        model = ConferenceInfo
        fields = ('room', 'user', 'conference_title', 'conference_description', )

    # def __init__(self):
    #     super().__init__()
    #     self.fields['start_date'].widget = widgets.AdminTimeWidget()
