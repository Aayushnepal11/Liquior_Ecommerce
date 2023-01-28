from django import forms

PRODUCT_COUNTER = [(i, str(i)) for i in range(1, 21)]


# print(PRODUCT_COUNTER)

class ADDtoCartForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_COUNTER,
        coerce=int
    )
    override = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput,
    )
