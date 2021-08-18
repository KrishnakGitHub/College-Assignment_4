from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Student, Department, Lecturer
# Create your views here.
def Index(request):
	return render(request,'myapp/student_list.html')

def get_queryset(request):
	query1 = request.GET.get('q1')
	query2 = request.GET.get('q2')


	object_list = Department.objects.all()

	stu_object_list = Student.objects.filter(name=query1)
	lec_object_list = Lecturer.objects.filter(name=query1)

	if query2 =='all':
		dep_stu_object_list = Student.objects.all()
		dep_lec_object_list = Lecturer.objects.all()
	else:
		dep_stu_object_list = Student.objects.filter(Department=query2)
		dep_lec_object_list = Lecturer.objects.filter(Department=query2)
	

	context = {'stu_object_list':stu_object_list,'lec_object_list':lec_object_list,
	'dep_stu_object_list':dep_stu_object_list,'dep_lec_object_list':dep_lec_object_list,'object_list':object_list}

	return render(request, 'myapp/student_list.html', context)