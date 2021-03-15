from django.shortcuts import render

from list_of_employees.models import Employees

def display_tree(request):
    '''
    отображает древо сотрудников
    - подразделение
    -- ранг
    --- сотрудник 1
    --- сотрудник 2
    --- ...
    --- сотрудник n

    '''
    depatrments_list = []
    all_employees = Employees.objects.all()
    for e in all_employees:
        if e.department not in depatrments_list:
            depatrments_list.append(e.department)
    depatrments_list.sort()

    positions = [
        'Team Leader',
        'Manager',
        'Assistant Manager',
        'Director',
        'Administrator'
        ]
    show_departments = None
    department = None
    position = None

    if request.method == 'GET':
        if 'show_departments' in request.GET:
            show_departments = request.GET['show_departments']
        if 'department' in request.GET:
            department = request.GET['department']
        if 'position' in request.GET:
            position = request.GET['position']
    employees = None
    if department and position:
        print(f"{'op'=}")
        employees = Employees.objects.filter(
            department=department,
            position=position.upper())
        print(f"{position=}")
        print(f"{employees=}")
    context = {
        'depatrments_list': depatrments_list,
        'positions': positions,
        'employees': employees,
        'show_departments': show_departments,
        'selected_department': department,
        'selected_position': position,
    }
    return render(
        request,
        'list_of_employees/index.html',
        context=context,
        )

