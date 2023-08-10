from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.forms.formsets import formset_factory

from .forms import GroupForm
from theme.forms import ThemeForm

def create_group(request):
    GroupFormSet = formset_factory(GroupForm)

    if request.method == 'GET':
        form = ThemeForm()
        formset = GroupFormSet()

        return render(request, 'group/create_group.html', {'form': form, 'formset': formset}) 
    elif request.method == 'POST':
        form = GroupForm(request.POST)
        formset = GroupFormSet(request.POST)
        if all([form.is_valid(), formset.is_valid()]):
            theme = form.save(commit=False)
            theme.save()
            return HttpResponseRedirect(reverse('theme:theme', args = (theme.id,)))
        else:
            return render(request, 'theme/create_theme.html', {'form': form})
