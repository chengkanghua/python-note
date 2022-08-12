from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from app01.models import Student
from django.forms import ModelForm
from django.http import JsonResponse


class StudentModelForm(ModelForm):
    class Meta:
        model = Student
        # fields = "__all__"
        # fields = ["name","age","email","birth"]
        exclude = ["createDate"]

        labels = {"name": "用户名", "age": "年龄"}

        from django.forms import widgets as wid
        widgets = {
            "name": wid.TextInput(attrs={"class": "form-control"}),
            "age": wid.NumberInput(attrs={"class": "form-control"}),
            "email": wid.EmailInput(attrs={"class": "form-control"}),
            "birth": wid.DateInput(attrs={"class": "form-control", "type": "date"})
        }


def index(request):
    students = Student.objects.all()

    return render(request, "index.html", {"students": students})


def addStu(request):
    if request.method == "GET":
        studentModelFormObj = StudentModelForm()

        return render(request, "addStu.html", {"studentModelFormObj": studentModelFormObj})
    else:
        # 添加功能
        studentModelFormObj = StudentModelForm(data=request.POST)

        if studentModelFormObj.is_valid():  # studentModelFormObj.cleaned_data  studentModelFormObj.errors
            studentModelFormObj.save()  # create()

            return redirect("/")
        else:
            print(studentModelFormObj.errors)
            return JsonResponse(studentModelFormObj.errors)


def editStu(request, edit_id):
    stu_object = Student.objects.get(pk=edit_id)

    if request.method == 'GET':
        studentModelFormObj = StudentModelForm(instance=stu_object)
        return render(request, "editStu.html", {"studentModelFormObj": studentModelFormObj})

    else:
        studentModelFormObj = StudentModelForm(data=request.POST,instance=stu_object)
        if studentModelFormObj.is_valid():
            studentModelFormObj.save() # update
            return redirect("/")

        else:
            print(studentModelFormObj.errors)
            return JsonResponse(studentModelFormObj.errors)




