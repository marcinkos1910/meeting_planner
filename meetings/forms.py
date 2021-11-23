from django import forms

from meetings import models


class MeetingForm(forms.ModelForm):
    class Meta:
        model = models.Meeting
        fields = '__all__'


class RoomForm(forms.ModelForm):
    class Meta:
        model = models.Room
        fields = '__all__'
