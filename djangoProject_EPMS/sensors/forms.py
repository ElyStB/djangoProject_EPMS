from django import forms

from djangoProject_EPMS.sensors.models import SensorModel


class SensorBaseForm(forms.ModelForm):
    class Meta:
        model = SensorModel
        fields = ('location_latitude', 'Location_longitude', 'type', 'serial_number','description', 'is_rented')
        widgets = {
            'location_latitude': forms.TextInput(attrs={'placeholder': 'Location_latitude'}),
            'Location_longitude': forms.Textarea(attrs={'placeholder': 'Location_longitude'}),
            'type': forms.Textarea(attrs={'placeholder': 'Sensor Type'}),
            'serial_number': forms.TextInput(attrs={'placeholder': 'Serial number'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'is_rented': forms.CheckboxInput(attrs={'placeholder': 'Is rented'}),
        }


class SensorCreateForm(SensorBaseForm):
    ...


class SensorEditForm(SensorBaseForm):
    ...


class SensorDeleteForm(SensorBaseForm):
    ...
