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

    ranks = ['I', 'II', 'III', 'IV', 'V']
    show_departments = None
    department = None
    rank = None

    if request.method == 'GET':
        if 'show_departments' in request.GET:
            show_departments = request.GET['show_departments']
        if 'department' in request.GET:
            department = request.GET['department']
        if 'rank' in request.GET:
            rank = request.GET['rank']
    employees = None
    if department and rank:
        employees = Employees.objects.filter(
            department=department,
            rank=rank)

    context = {
        'depatrments_list': depatrments_list,
        'ranks': ranks,
        'employees': employees,
        'show_departments': show_departments,
        'selected_department': department,
        'selected_rank': rank,
    }
    return render(
        request,
        'list_of_employees/index.html',
        context=context,
        )

