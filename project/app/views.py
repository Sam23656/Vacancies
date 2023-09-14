from django.core.paginator import Paginator
from django.shortcuts import render
# Create your views here.
from django.views.generic import ListView, DetailView

from app.models import *

from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Job, Company


def view_func(request):
    jobs = Job.objects.all()

    company_filter = request.GET.get('company_filter')
    vacancy_filter = request.GET.get('vacancy_filter')
    status_filter = request.GET.get('status_filter')

    if company_filter != "":
        jobs = jobs.filter(company__name=company_filter)

    if vacancy_filter != "":
        jobs = jobs.filter(title__title=vacancy_filter)

    if status_filter != "":
        jobs = jobs.filter(title__title__startswith=status_filter)

    paginator = Paginator(jobs, 10)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "paginator": paginator,
        "companies": Company.objects.all(),
        "selected_company": company_filter,
        "titles": VacancyTitle.objects.all(),
    }

    return render(request, "app/vacancy_list.html", context=context)


class ViewClass(ListView):
    paginate_by = 3
    template_name = 'app/vacancy_list.html'
    model = Job


class DetailViewClass(DetailView):
    model = Job
    template_name = 'app/detail_view.html'
    context_object_name = 'job'
    slug_field = 'slug'
