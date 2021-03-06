from django.shortcuts import render, HttpResponse
from django import forms
from app01 import models
from django.forms import formset_factory


class MultiPermissionForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"})
    )
    url = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"})
    )
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"})
    )
    menu_id = forms.ChoiceField(
        choices=[(None, '-----')],
        widget=forms.Select(attrs={'class': "form-control"}),
        required=False,

    )

    pid_id = forms.ChoiceField(
        choices=[(None, '-----')],
        widget=forms.Select(attrs={'class': "form-control"}),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['menu_id'].choices += models.Menu.objects.values_list('id', 'title')
        self.fields['pid_id'].choices += models.Permission.objects.filter(pid__isnull=True).exclude(
            menu__isnull=True).values_list('id', 'title')


class MultiUpdatePermissionForm(forms.Form):
    id = forms.IntegerField(
        widget=forms.HiddenInput()
    )
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"})
    )
    url = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"})
    )
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"})
    )
    menu_id = forms.ChoiceField(
        choices=[(None, '-----')],
        widget=forms.Select(attrs={'class': "form-control"}),
        required=False,

    )

    pid_id = forms.ChoiceField(
        choices=[(None, '-----')],
        widget=forms.Select(attrs={'class': "form-control"}),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['menu_id'].choices += models.Menu.objects.values_list('id', 'title')
        self.fields['pid_id'].choices += models.Permission.objects.filter(pid__isnull=True).exclude(
            menu__isnull=True).values_list('id', 'title')


def multi_add(request):
    """
    ????????????
    :param request:
    :return:
    """
    formset_class = formset_factory(MultiPermissionForm, extra=2)

    if request.method == 'GET':
        formset = formset_class()
        return render(request, 'multi_add.html', {'formset': formset})

    formset = formset_class(data=request.POST)
    if formset.is_valid():
        flag = True
        post_row_list = formset.cleaned_data  # ??????formset???????????????????????????????????????????????????????????????
        for i in range(0, formset.total_form_count()):
            row = post_row_list[i]
            if not row:
                continue
            try:
                obj = models.Permission(**row)
                obj.validate_unique()  # ????????????????????????????????????????????????????????????
                obj.save()
            except Exception as e:
                formset.errors[i].update(e)
                flag = False
        if flag:
            return HttpResponse('????????????')
        else:
            return render(request, 'multi_add.html', {'formset': formset})
    return render(request, 'multi_add.html', {'formset': formset})


def multi_edit(request):
    formset_class = formset_factory(MultiUpdatePermissionForm, extra=0)
    if request.method == 'GET':
        formset = formset_class(
            initial=models.Permission.objects.all().values('id', 'title', 'name', 'url', 'menu_id', 'pid_id'))
        return render(request, 'multi_edit.html', {'formset': formset})

    formset = formset_class(data=request.POST)
    if formset.is_valid():
        post_row_list = formset.cleaned_data  # ??????formset???????????????????????????????????????????????????????????????
        flag = True
        for i in range(0, formset.total_form_count()):
            row = post_row_list[i]
            if not row:
                continue
            permission_id = row.pop('id')
            try:
                permission_object = models.Permission.objects.filter(id=permission_id).first()
                for key, value in row.items():
                    setattr(permission_object, key, value)
                permission_object.validate_unique()
                permission_object.save()

            except Exception as e:
                formset.errors[i].update(e)
                flag = False
        if flag:
            return HttpResponse('????????????')
        else:
            return render(request, 'multi_edit.html', {'formset': formset})
    return render(request, 'multi_edit.html', {'formset': formset})
