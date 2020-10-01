from user.forms import ContactUsForm, UserForm
from user.models import User
# from user.utils import smth_slow, old_logs
from user.tasks import old_logs_async, smth_slow_async

from django.shortcuts import get_object_or_404, redirect, render


def creat_users(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-name')
    elif request.method == 'GET':
        form = UserForm()
    context = {'user_form': form}
    return render(request, 'create_user.html', context=context)


def users(request):
    context = {'user_list': User.objects.all()}
    return render(request, 'list_user.html', context=context)


def update_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-name')
    elif request.method == 'GET':
        form = UserForm(instance=user)
    context = {'user_form': form,
               'user_instance': user
               }
    return render(request, 'create_user.html', context=context)


def slow(request):
    smth_slow_async.delay()
    return render(request, 'index.html')


def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-name')
    elif request.method == 'GET':
        form = ContactUsForm()
    context = {'form': form}
    return render(request, 'contact_us.html', context=context)


def log(request):
    old_logs_async.delay()
    return render(request, 'index.html')
