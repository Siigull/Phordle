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
        form = ThemeForm(request.POST)
        formset = GroupFormSet(request.POST)
        if all([form.is_valid(), formset.is_valid()]):
            theme = form.save()
            for inline_form in formset:
                if inline_form.cleaned_data:
                    group = inline_form.save(commit=False)
                    group.theme = theme
                    group.save()
            return redirect('profile')
        else:
            return render(request, 'group/create_group.html', {'form': form})
