from django import forms

from .models import ContactMessage, Driver, Vehicle


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = [
            'vehicle_number',
            'make',
            'model',
            'year',
            'vehicle_type',
            'owner_name',
            'driver',
            'status',
            'last_service_date',
            'next_service_date',
            'repair_notes',
            'service_cost',
        ]
        widgets = {
            'vehicle_number': forms.TextInput(attrs={'placeholder': 'KA-01-AB-1234'}),
            'make': forms.TextInput(attrs={'placeholder': 'Toyota'}),
            'model': forms.TextInput(attrs={'placeholder': 'Innova'}),
            'vehicle_type': forms.TextInput(attrs={'placeholder': 'Car, Van, Truck'}),
            'owner_name': forms.TextInput(attrs={'placeholder': 'Owner or driver name'}),
            'last_service_date': forms.DateInput(attrs={'type': 'date'}),
            'next_service_date': forms.DateInput(attrs={'type': 'date'}),
            'repair_notes': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Service notes, repairs, parts replaced'}),
            'service_cost': forms.NumberInput(attrs={'placeholder': '0.00', 'step': '0.01'}),
        }


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'your@email.com'}),
            'message': forms.Textarea(attrs={'rows': 5, 'placeholder': 'How can we help?'}),
        }


class DriverForm(forms.ModelForm):
    assigned_vehicles = forms.ModelMultipleChoiceField(
        queryset=Vehicle.objects.none(),
        required=False,
        widget=forms.SelectMultiple(attrs={'size': 6}),
        help_text='Select one or more vehicles assigned to this driver. Hold Ctrl to choose multiple vehicles.',
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['assigned_vehicles'].queryset = Vehicle.objects.order_by('vehicle_number')
        if self.instance.pk:
            self.fields['assigned_vehicles'].initial = self.instance.vehicles.all()

    class Meta:
        model = Driver
        fields = ['name', 'license_number', 'phone', 'experience_years', 'is_available', 'assigned_vehicles']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Driver name'}),
            'license_number': forms.TextInput(attrs={'placeholder': 'DL-KA-2020-1001'}),
            'phone': forms.TextInput(attrs={'placeholder': '9876501001'}),
            'experience_years': forms.NumberInput(attrs={'min': 0, 'placeholder': '5'}),
        }

    def save(self, commit=True):
        driver = super().save(commit=commit)
        if commit:
            selected_vehicles = self.cleaned_data.get('assigned_vehicles')
            selected_ids = list(selected_vehicles.values_list('pk', flat=True))
            driver.vehicles.exclude(pk__in=selected_ids).update(driver=None)
            Vehicle.objects.filter(pk__in=selected_ids).update(driver=driver)
        return driver
