from django.shortcuts import render, get_object_or_404

from .models import Problem


def Home(request):
    template_name = 'index.html'

    objs = list(Problem.objects.all())
    tpl_obj = {'objs': objs}

    return render(request, template_name, tpl_obj)


def problem(request, problem_id):
    problem_obj = get_object_or_404(Problem, pk=problem_id)

    if problem_obj.id == 1:
        previous_problem = None
        next_problem = get_object_or_404(Problem, pk=problem_id + 1)
    elif problem_obj.id == Problem.objects.count():
        previous_problem = get_object_or_404(Problem, pk=problem_id - 1)
        next_problem = None
    else:
        next_problem = get_object_or_404(Problem, pk=problem_id + 1)
        previous_problem = get_object_or_404(Problem, pk=problem_id - 1)

    tpl_obj = {'problem_obj': problem_obj,
               'previous_problem': previous_problem,
               'next_problem': next_problem,
               'count_obj' : Problem.objects.count()
               }
    return render(request, 'problem/problem.html', tpl_obj)
