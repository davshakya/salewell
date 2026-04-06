from django import forms

from .models import Lead


class LeadForm(forms.ModelForm):
    interest = forms.ChoiceField(
        choices=[("", "Select a collection")] + Lead.INTEREST_CHOICES,
    )

    class Meta:
        model = Lead
        fields = ["name", "email", "interest", "message"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Your name",
                    "autocomplete": "name",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "you@example.com",
                    "autocomplete": "email",
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "placeholder": "Tell us the styles, colors, sizes, or occasion you are shopping for.",
                    "rows": 6,
                }
            ),
        }
