from django import forms

from .models import Lead, Order


class LeadForm(forms.ModelForm):
    interest = forms.ChoiceField(
        choices=[("", "Select your requirement")] + Lead.INTEREST_CHOICES,
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
                    "placeholder": "Share tank capacity, motor HP, number of tanks, property type, or installation questions.",
                    "rows": 6,
                }
            ),
        }


class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(
        min_value=1,
        max_value=10,
        initial=1,
        widget=forms.NumberInput(
            attrs={
                "min": 1,
                "max": 10,
            }
        ),
    )


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "customer_name",
            "email",
            "phone",
            "address_line1",
            "address_line2",
            "city",
            "state",
            "postal_code",
            "delivery_area",
            "notes",
        ]
        widgets = {
            "customer_name": forms.TextInput(attrs={"placeholder": "Full name"}),
            "email": forms.EmailInput(attrs={"placeholder": "you@example.com"}),
            "phone": forms.TextInput(attrs={"placeholder": "+91 98765 43210"}),
            "address_line1": forms.TextInput(attrs={"placeholder": "House no, street, locality"}),
            "address_line2": forms.TextInput(attrs={"placeholder": "Landmark, apartment, optional"}),
            "city": forms.TextInput(attrs={"placeholder": "City"}),
            "state": forms.TextInput(attrs={"placeholder": "State"}),
            "postal_code": forms.TextInput(attrs={"placeholder": "PIN / ZIP code"}),
            "delivery_area": forms.TextInput(attrs={"placeholder": "India"}),
            "notes": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Mention tank capacity, motor HP, wiring notes, preferred call time, or installation support needed.",
                }
            ),
        }


class OrderLookupForm(forms.Form):
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={"placeholder": "Use the email you placed the order with"}),
    )
    order_number = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Order number, for example SWT-20260407-ABC123"}),
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        order_number = cleaned_data.get("order_number")
        if not email and not order_number:
            raise forms.ValidationError("Enter your email or order number to view orders.")
        return cleaned_data
