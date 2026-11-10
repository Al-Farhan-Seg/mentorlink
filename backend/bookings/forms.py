from django import forms
from .models import Booking
from django.utils import timezone

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["slot", "subject", "notes"]

    def clean(self):
        
        cleaned_data = super().clean()
        slot = cleaned_data.get("slot")
        subject = cleaned_data.get("subject")
        

        if slot and subject and not slot.tutor.subjects.filter(pk=subject.pk).exists():
            raise forms.ValidationError(
                "This tutor does not teach the selected subject."
            )

        if slot and slot.start_at <= timezone.now():
            raise forms.ValidationError(
                "The selected slot has either passed or it has already started"
            )

        return cleaned_data
            
