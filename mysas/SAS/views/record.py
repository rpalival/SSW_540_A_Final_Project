from django.shortcuts import render, redirect
from django import forms
from SAS import models
from SAS.models import UserInfo, Attendance


class TeacherModelForm(forms.ModelForm):
    class Meta:
        model = models.Attendance
        fields = ["studentID", "attendance", "date", "starttime", "grade"]


class SlotModelForm(forms.ModelForm):
    class Meta:
        model = models.Attendance
        fields = ["date", "starttime"]


def teacher(request):
    studentid = request.session.get('info')
    if not studentid:
        return redirect('/login/')
    account_object = UserInfo.objects.filter(studentID=studentid).first()

    return render(request, "teacher.html", {"obj": account_object})


def bookSlot(request):
    studentid = request.session.get('info')
    if not studentid:
        return redirect('/login/')
    account_obj = UserInfo.objects.filter(studentID=studentid).first()
    attend_obj = Attendance.objects.filter(studentID=studentid)
    # for item in attend_obj:
    #     print(item.studentID)
    if request.method == "GET":
        form = SlotModelForm()
        return render(request, "bookSlot.html", {"attend_obj": attend_obj,
                                                 "form": form})
    form = SlotModelForm(data=request.POST)
    if form.is_valid():
        newdate = form.cleaned_data.get("date")
        newtime = form.cleaned_data.get("starttime")
        # date_obj =
        Attendance.objects.create(studentID=studentid,
                                  classname=account_obj.classname,
                                  date=newdate,
                                  starttime=newtime,
                                  attendance="NO",
                                  grade=0
                                  )
        return render(request, "bookSlot.html", {"attend_obj": attend_obj,
                                                 "form": form})
    form.add_error("starttime", "Date or Time is unavailable")
    return render(request, "bookSlot.html", {"attend_obj": attend_obj,
                                             "form": form})


def teacherAttendance(request):
    studentid = request.session.get('info')
    if not studentid:
        return redirect('/login/')
    attend_obj = Attendance.objects.all()
    # print(obj)
    if request.method == "GET":
        form = TeacherModelForm()
        return render(request, "teacherAttendance.html", {"obj": attend_obj, "form": form})
    form = TeacherModelForm(data=request.POST)
    # print(form)
    if form.is_valid():
        newID = form.cleaned_data.get("studentID")
        newatt = form.cleaned_data.get("attendance")
        newDate = form.cleaned_data.get("date")
        newTime = form.cleaned_data.get("starttime")
        newGrade = form.cleaned_data.get("grade")
        new_obj = Attendance.objects.filter(studentID=newID,
                                            date=newDate,
                                            starttime=newTime)
        # print(new_obj)
        if not new_obj:
            form.add_error("grade", "Confirmation Failed")
            return render(request, "teacherAttendance.html", {"obj": attend_obj, "form": form})
        Attendance.objects.filter(studentID=newID,
                                  date=newDate,
                                  starttime=newTime).update(attendance=newatt)
        Attendance.objects.filter(studentID=newID,
                                  date=newDate,
                                  starttime=newTime).update(grade=newGrade)
        return render(request, "teacherAttendance.html", {"obj": attend_obj, "form": form})

    form.add_error("grade", "Invalid Input")
    return render(request, "teacherAttendance.html", {"obj": attend_obj, "form": form})
