from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic 
from django.contrib.auth.models import User

from django.forms.formsets import formset_factory

from .forms import GroupForm, AddUserForm
from theme.forms import ThemeForm
from group.models import Group

def create_group(request):
    GroupFormSet = formset_factory(GroupForm)

    if request.method == 'GET':
        form = ThemeForm()
        formset = GroupFormSet()

        return render(request, 'group/create_group.html', {'form': form, 'formset': formset}) 
    elif request.method == 'POST':
        form = ThemeForm(request.POST)
        formset = GroupFormSet(request.POST)
        if all([form.is_valid(), formset.is_valid()]):
            theme = form.save()
            for inline_form in formset:
                if inline_form.cleaned_data:
                    group = inline_form.save(commit=False)
                    group.theme = theme
                    group.save()
                    group.users.set([request.user.pk])
            return redirect('profile')
        else:
            return render(request, 'group/create_group.html', {'form': form})

def group(request, pk):
    group = Group.objects.get(pk=pk)

    if request.method == 'GET':
        form = AddUserForm()

        return render(request, 'group/detail.html', {'form': form, 'group': group})
    elif request.method == 'POST':
        result_form = AddUserForm(request.POST)
        form = AddUserForm()
        try:
            user = User.objects.filter(username=result_form.data['add_user'])[0]
        except IndexError:
            return render(request, 'group/detail.html', {'form':form, 'group': group, 'err':True})

        group.users.set([user.pk])

        form = AddUserForm()

        return render(request, 'group/detail.html', {'form': form, 'group': group})


class GroupList(generic.ListView):
    template_name = 'user/group_list.html'
    context_object_name = 'user_groups'

    def get_queryset(self):
        return Group.objects.filter(users=self.request.user.id).all()

def group_theme(request, pk):
    theme = Group.objects.get(pk=pk).theme

    return render(request, 'group/group_theme', {})
