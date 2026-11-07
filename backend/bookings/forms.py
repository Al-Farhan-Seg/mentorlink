from django import forms
from .models import Booking

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

        return cleaned_data
            
