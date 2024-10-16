from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse,redirect
from .models import Student,Teacher,User
from django.contrib.auth import authenticate,logout,login

# Create your views here.
def home(request):
     return render(request,"home.html")

def adminhome(request):
     return render(request,"admin_page.html")

def teacherhome(request):
     return render(request,"teacher_home.html")
def studenthome(request):
     return render(request,"studenthome.html")

def student_register(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        address=request.POST['address']
        email=request.POST['email']
        phone=request.POST['phone']
        guardian=request.POST['guardian']
        username=request.POST['username']
        password=request.POST['password']

        student_user=User.objects.create_user(first_name=firstname,last_name=lastname,email=email,
                                  username=username,password=password,usertype='student',is_active=False)
        student_user.save()
        x=Student.objects.create(student_id=student_user,address=address,phone=phone,guardian=guardian)
        x.save()
        return redirect(home)
    else:
        return render(request,"student_register.html")
    
def view_stud_profile(request):
    x=Student.objects.all()
    return render(request,"view_stud_profile.html",{"view":x})

def view_teachers(request):
    x=Teacher.objects.all()
    return render(request,"view_teachers.html",{"view":x})
    
def view_student(request):
    x=Student.objects.all()
    return render(request,"view_student.html",{"view":x})

def delete_student(request,id):
    x=Student.objects.get(id=id)
    x.delete()
    return redirect(view_student)

def edit_student(request):
    id=request.session['student_id']
    edits=Student.objects.get(student_id=id)
    return render(request,"edit_student.html",{'edit':edits})

def update_student(request,id):
  
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        address=request.POST['address']
        email=request.POST['email']
        phone=request.POST['phone']
        guardian=request.POST['guardian']
        # username=request.POST['username']
        # password=request.POST['password']
        x=User.objects.get(id=id)
        y=Student.objects.get(student_id=id)
        x.first_name=firstname
        x.last_name=lastname
        y.address=address
        x.email=email
        y.phone=phone
        y.guardian=guardian
        # x.username=username
        # x.password=password
        x.save()
        y.save()
        return redirect(studenthome)

    
def teacher(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        address=request.POST['address']
        email=request.POST['email']
        phone=request.POST['phone']
        salary=request.POST['salary']
        experience=request.POST['experience']
        username=request.POST['username']
        password=request.POST['password']

        teacher_user=User.objects.create_user(first_name=firstname,last_name=lastname,email=email,
                                  username=username,password=password,usertype='teacher',is_active=True,is_staff=True)
        teacher_user.save()
        x=Teacher.objects.create(teacher_id=teacher_user,address=address,phone=phone,salary=salary,experience=experience)
        x.save()
        return redirect(adminhome)
    else:
        return render(request,"teacher_register.html")

def view_teacher_profile(request):
    x=Teacher.objects.all()
    return render(request,"view_teacher_profile.html",{"view":x})

    
def view_teacher(request):
    x=Teacher.objects.all()
    return render(request,"view_teacher.html",{"view":x})

def delete_teacher(request,id):
    x=Teacher.objects.get(id=id)
    x.delete()
    return redirect(view_teacher)

def view_students(request):
    x=Student.objects.all()
    return render(request,"view_students.html",{"view":x})

def edit_teacher(request):
    id=request.session['teacher_id']
    edits=Teacher.objects.get(teacher_id=id)
    return render(request,"edit_teacher.html",{'edit':edits})

def update_teacher(request,id):
  
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        address=request.POST['address']
        email=request.POST['email']
        phone=request.POST['phone']
        salary=request.POST['salary']
        experience=request.POST['experience']
        # username=request.POST['username']
        # password=request.POST['password']
        x=User.objects.get(id=id)
        y=Teacher.objects.get(teacher_id=id)
        x.first_name=firstname
        x.last_name=lastname
        y.address=address
        x.email=email
        y.phone=phone
        y.salary=salary
        y.experience=experience
        # x.username=username
        # x.password=password
        x.save()
        y.save()
        return redirect(teacherhome)

def logins(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        userpassword=authenticate(request,username=username,password=password)
        print(username)
        print(password)
        print(userpassword)
        if userpassword is not None and userpassword.is_superuser==1:
            return redirect(adminhome)
            # return render(request,"admin_page.html")
        elif userpassword is not None and userpassword.is_staff==1:
            login(request,userpassword)
            request.session['teacher_id']=userpassword.id
            return redirect(teacherhome)
        elif userpassword is not None and userpassword.is_active==1:
            login(request,userpassword)
            request.session['student_id']=userpassword.id
            return redirect(studenthome)
        else:
            return HttpResponse("invalid login")

    else:
        return render(request,"login.html")
    
def approve_student(request,id):
    print(id)
    s=Student.objects.select_related('student_id').get(id=id)
    print(s)
    s.student_id.is_active=True
    s.student_id.save()
    return redirect(view_student)
    # return HttpResponse("ok")


def logouts(request):
    logout(request)
    return redirect(home)  
