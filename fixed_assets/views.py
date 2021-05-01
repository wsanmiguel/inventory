from django.shortcuts import render, redirect

from django.http import HttpResponse, JsonResponse

from .models import DocumentType, Third
from .forms import DocumentTypeForm, ThirdForm
# Create your views here.


def home(request):
    context = {}
    return render(request, 'home.html', context)

#### Tipos de Documento
def document_types(request):
    list_document_types = DocumentType.objects.all()
    context = {
        'title': 'Tipos de Documento',
        'document_types': list_document_types
    }

    return render(request, 'document_type/document_types.html', context)


def get_document_type(request, id):
    document_type = DocumentType.objects.filter(id=id).first()
    context = {
        'title': 'Tipo de Documento',
        'document_type': document_type
    }

    return render(request, 'document_type/detail_document_type.html', context)

def new_document_type(request):
    form = DocumentTypeForm()
    if request.method == 'POST':
        form = DocumentTypeForm(request.POST)

        if form.is_valid():
            DocumentType(
                id = form.cleaned_data['id'],
                name =  form.cleaned_data['name']
                #active= form.cleaned_data['active']
            ).save()
            return redirect('document_types')

    return render(request, 'document_type/new_document_type.html', {'form': form})

#### Terceros
def thirds(request):
    list_thirds = Third.objects.all()
    context = {
        'title': 'Terceros',
        'thirds': list_thirds
    }

    return render(request, 'third/thirds.html', context)


def get_third(request, id):
    third = Third.objects.filter(identification=id).first()
    context = {
        'title': 'Tercero',
        'third': third,
    }

    return render(request, 'third/detail_third.html', context)

def new_third(request):
    document_types = DocumentType.objects.all().values_list('id', 'name')
    form = ThirdForm(document_types_choices= document_types)
    if request.method == 'POST':
        form = ThirdForm(request.POST,document_types_choices= document_types)

        if form.is_valid():
            document_type = DocumentType.objects.filter(id=form.cleaned_data['document_type']).first()
            data = {'document_type': form.cleaned_data['document_type'],
                'identification': form.cleaned_data['identification'],
                'first_name' : form.cleaned_data['first_name'],
                'last_name' : form.cleaned_data['last_name'],
                'phone' : form.cleaned_data['phone'],
                'address' : form.cleaned_data['address'],
                'birthday' : form.cleaned_data['birthday'],
            }
            print(data)
            Third(
                document_type = document_type,
                identification = form.cleaned_data['identification'],
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                phone = form.cleaned_data['phone'],
                address = form.cleaned_data['address'],
                birthday = form.cleaned_data['birthday']
            ).save()
            return redirect('thirds')

    return render(request, 'third/new_third.html', {'form': form})

# def new_document_type(request):
#     group_choices = Group.objects.all().values_list('id', 'title')
#     form = StudenFrom(group_choices=group_choices)
#     if request.method == 'POST':
#         form = StudenFrom(request.POST, group_choices=group_choices)

#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             group_choices = form.cleaned_data['group']

#             student = Student(first_name=first_name, last_name=last_name)
#             student.save()

#             student.group.add(group_choices)

#             return redirect('students')

#     return render(request, 'student/new_student.html', {'form': form})

# def list_document_types(request):
#     response = get_document_types()
#     return JsonResponse(response)


# def get_document_types():
#     document_types = DocumentType.objects.all()
#     response = {}
#     for document_type in document_types:
#         print(student.first_name, student.last_name)
#         response[student.id] = {
#             'full name': '{} {}'.format(student.first_name, student.last_name),
#         }
#         enrollments = student.enrollment_set.all()
#         student_enrollment = []

#         for enrollment in enrollments:

#             average_enrollment = 0
#             notes = enrollment.note_set.all()
#             if notes:
#                 for note in notes:
#                     average_enrollment = average_enrollment + note.value

#                 average_enrollment = average_enrollment / len(notes)
#             student_enrollment.append(
#                 {
#                     'name': enrollment.subject.name,
#                     'average': average_enrollment
#                 }
#             )

#         response[student.id]['enrollments'] = student_enrollment
#     return response





# def groups(request):
#     groups = Group.objects.all()
#     context = {
#         'title': 'Groups',
#         'groups': groups
#     }

#     return render(request, 'group/list_groups.html', context)

# def get_group(request, id):

#     group = Group.objects.filter(id=id).first()
#     students = group.student_set.all()
#     context = {
#         'title': group.title,
#         'group': group,
#         'students': students
#     }

#     return render(request, 'group/detail_group.html', context)

# def new_group(request):
#     form = GroupForm()
#     if request.method == 'POST':
#         form = GroupForm(request.POST)

#         if form.is_valid():
#             description = form.cleaned_data['description']
#             title = form.cleaned_data['title']

#             Group(title=title, description=description).save()
#             return redirect('groups')

#     return render(request, 'group/new_group.html', {'form': form})


# def teachers(request):
#     teachers = Teacher.objects.all()
#     context = {
#         'title': 'Profesores',
#         'teachers': teachers
#     }

#     return render(request, 'teacher/list_teachers.html', context)

# def get_teacher(request, id):
#     teacher = Teacher.objects.filter(id=id).first()
#     context = {
#         'title': 'teacher',
#         'teacher': teacher
#     }

#     return render(request, 'teacher/detail_teacher.html', context)

# def new_teacher(request):
#     form = TeacherFrom()
#     if request.method == 'POST':
#         form = TeacherFrom(request.POST)

#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']

#             teacher = Teacher(first_name=first_name, last_name=last_name)
#             teacher.save()


#             return redirect('teachers')

#     return render(request, 'teacher/new_teacher.html', {'form': form})


# def list_person(request, person):
#     models = Student
#     if person == 'teacher':
#         models = Teacher

#     persons = models.objects.all()
#     context = {
#         'title': person,
#         'persons': persons
#     }
#     return render(request, 'person/list_person.html', context)

# def get_person(request, person, id):
#     models = Student
#     if person == 'teacher':
#         models = Teacher

#     persons = models.objects
#     person = persons.filter(id=id).first()
#     context = {
#         'title': person,
#         'person': person
#     }
#     return render(request, 'person/person_detail.html', context)