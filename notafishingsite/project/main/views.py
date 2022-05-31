from django.shortcuts import render, redirect, Http404
from .models import Job
from .forms import JobForm
from django.views.generic import DetailView, UpdateView, DeleteView


def index(request):
    jobs = Job.objects.order_by('-id')

    return render(request, 'main/index.html', {'title': 'Главная страница сайта',
                                               'jobs': jobs})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Некорректное заполнение формы.'

    form = JobForm()
    context = {'form': form,
               'error': error}
    return render(request, 'main/create.html', context)


class Details(DetailView):
    model = Job
    template_name = 'main/details.html'
    context_object_name = 'job'


class Update(UpdateView):
    model = Job
    template_name = 'main/create.html'
    form_class = JobForm



class Delete(DeleteView):
    model = Job
    success_url = '/create'
    template_name = 'main/delete.html'




