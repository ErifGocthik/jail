from django.http import HttpResponseRedirect
from django.shortcuts import render

from sitejail.models import Prisoner

from .forms import PrisonerForm


def post_main(request):
    point = Prisoner.objects.all()
    context = {'points': point}
    return render(request, 'main-page/Main.html', context)


def post_form(request):
    form = PrisonerForm()
    return render(request, 'main-page/Form.html', {'form': form})
