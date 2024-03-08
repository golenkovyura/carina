from django import forms


class TaskForm(forms.Form):
    x = forms.FloatField(label="Введите x")
    y = forms.FloatField(label="Введите y")