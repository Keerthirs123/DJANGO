from django.shortcuts import render


# Create your views here.
students={
   "John":{'Maths': 90,'Science':80,'English':70 },
    "Doe":{'Maths': 70,'Science':60,'English':50} ,
    "Smith":{'Maths': 80,'Science':70,'English':60} ,
    "Jane":{'Maths': 60,'Science':50,'English':40 },
    "Emily":{'Maths': 95,'Science':85,'English':75} ,
}

def home(request):
    return render(request,'school/home.html',{'students':students})

def result(request,name):
    result_text=students.get(name,"Result not found")
    return render(request,'school/result.html', {'name':name,'result':result_text})