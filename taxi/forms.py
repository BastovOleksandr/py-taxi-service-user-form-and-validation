from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

from taxi.models import Driver, Car
from taxi.validation_patterns import (
    LICENSE_NUMBER_PATTERN,
    LICENSE_NUMBER_HELP_TEXT,
    LICENSE_NUMBER_MESSAGE,
)


class DriverCreationForm(UserCreationForm):
    license_number = forms.CharField(
        required=True,
        validators=[
            RegexValidator(
                LICENSE_NUMBER_PATTERN,
                message=LICENSE_NUMBER_MESSAGE
            ),
        ],
        help_text=LICENSE_NUMBER_HELP_TEXT
    )
    cars = forms.ModelMultipleChoiceField(
        queryset=Car.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Driver
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "email",
            "license_number",
            "cars"
        )


class DriverLicenseUpdateForm(forms.ModelForm):
    license_number = forms.CharField(
        required=True,
        validators=[
            RegexValidator(
                LICENSE_NUMBER_PATTERN,
                message=LICENSE_NUMBER_MESSAGE
            ),
        ],
        help_text=LICENSE_NUMBER_HELP_TEXT
    )

    class Meta:
        model = Driver
        fields = ("license_number",)


class CarCreationForm(forms.ModelForm):
    drivers = forms.ModelMultipleChoiceField(
        queryset=Driver.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Car
        fields = ("model", "manufacturer", "drivers",)


class CarUpdateForm(forms.ModelForm):
    drivers = forms.ModelMultipleChoiceField(
        queryset=Driver.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Car
        fields = ("model", "manufacturer", "drivers",)
