from django import forms


class DatetimePickerInput(forms.TextInput):
    template_name = 'stark/forms/widgets/datetimepicker.html'
