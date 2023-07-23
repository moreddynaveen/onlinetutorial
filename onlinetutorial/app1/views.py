from django.shortcuts import render
def index(request):
    return render(request,'app1/index.html')
def cinfo(request):
    head_msg="ABOUT C LANGUAGE INFORMATION"
    msg1="Father of C language is DENNIES RITCHIE"
    msg2="It was created in the 1970s"
    msg3="C was  originally developed at Bell Labs"
    msg4="It is a functional programming language"
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3,'msg4':msg4}
    return render(request,'app1/profile1.html',context=my_dict)
def javainfo(request):
    head_msg="ABOUT JAVA LANGUAGE INFORMATION"
    msg1="Father of Java language is JAMES GOSLING"
    msg2="java is a class-based,object-oriented programming lanaguage"
    msg3="Java was released in may 1995"
    msg4="JDK means Java Development Kit"
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3,'msg4':msg4}
    return render(request,'app1/profile2.html',context=my_dict)
def pythoninfo(request):
    head_msg="ABOUT PYTHON LANGUAGE INFORMATION"
    msg1="Father of Python lanaguage GUIDO VAN ROSSUM"
    msg2="python is dynamically and garbage-collected."
    msg3="python is both object oriented and functional programming language"
    msg4="python syntax is very easy"
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3,'msg4':msg4}
    return render(request,'app1/profile3.html',context=my_dict)
def jsinfo(request):
    head_msg="ABOUT JAVASCRIPT LANGUAGE INFORMATION"
    msg1="Father of JS is BRENDAN EICH"
    msg2="JS engines were originally used only in web browsers"
    msg3="It is first web browser with graphical user interface"
    msg4="The most popular runtime system for this usage is Node.js."
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3,'msg4':msg4}
    return render(request,'app1/profile4.html',context=my_dict)


# Create your views here.
