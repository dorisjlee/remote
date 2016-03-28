from django.http import Http404
from django.shortcuts import get_object_or_404, render

from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import loader
from .models import Question, Round, Edge, Bulge, Bar, Pattern, Sa, Sa_num, Prominence, Tidal, Odd, Parent
from django.views import generic
from django.contrib.auth.models import User


class IndexView(generic.ListView):
    template_name = 'galaxyzoo/index.html'
    context_object_name = 'question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.all()


class DetailView(generic.DetailView):
    model = Question
    template_name = 'galaxyzoo/detail.html'


class ResultsView(generic.DetailView):
    model = Odd
    template_name = 'galaxyzoo/results.html'

class ParentView(generic.DetailView):
    model = Parent
    template_name = 'galaxyzoo/parent.html'

class RoundView(generic.DetailView):
    model = Round
    template_name = 'galaxyzoo/round.html'

class OddView(generic.DetailView):
    model = Odd
    template_name = 'galaxyzoo/odd.html'

class TidalView(generic.DetailView):
    model = Tidal
    template_name = 'galaxyzoo/tidal.html'

class ProminenceView(generic.DetailView):
    model = Prominence
    template_name = 'galaxyzoo/prominence.html'

class Sa_numView(generic.DetailView):
    model = Sa_num
    template_name = 'galaxyzoo/sa_num.html'

class SaView(generic.DetailView):
    model = Sa
    template_name = 'galaxyzoo/sa.html'

class PatternView(generic.DetailView):
    model = Pattern
    template_name = 'galaxyzoo/pattern.html'

class BarView(generic.DetailView):
    model = Bar
    template_name = 'galaxyzoo/bar.html'

class BulgeView(generic.DetailView):
    model = Bulge
    template_name = 'galaxyzoo/bulge.html'

class EdgeView(generic.DetailView):
    model = Edge
    template_name = 'galaxyzoo/edge.html'

# IMPORTANT back-end communication. Should go inside to_XX later.
    # print request.POST
    # question = get_object_or_404(Question, pk=question_id)
    # try:
    #     selected_choice = question.choice_set.get(pk=request.POST['choice'])
    # except (KeyError, Choice.DoesNotExist):
    #     # Redisplay the question voting form.
    #     return render(request, 'galaxyzoo/round.html', {
    #         'question': question,
    #         'error_message': "You didn't select a choice.",
    #     })
    # else:
    #     selected_choice.votes += 1
    #     selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.

def create_user(request, question_id):
    new = User.objects.create_user('%d' % User.objects.all().count())
    new.save()
    return HttpResponseRedirect(reverse('galaxyzoo:parent', args=(3,)))

def restart(request,question_id):
    return HttpResponseRedirect(reverse('galaxyzoo:parent', args=(3,)))

def vote(request, question_id):
    return HttpResponseRedirect(reverse('galaxyzoo:results', args=(1,)))

def to_round(request, question_id):

    return HttpResponseRedirect(reverse('galaxyzoo:round', args=(1,)))

def to_edge(request, question_id):

    return HttpResponseRedirect(reverse('galaxyzoo:edge', args=(1,)))

def to_bulge(request, question_id):

    return HttpResponseRedirect(reverse('galaxyzoo:bulge', args=(1,)))

def to_bar(request, question_id):

    return HttpResponseRedirect(reverse('galaxyzoo:bar', args=(1,)))

def to_pattern(request, question_id):

    return HttpResponseRedirect(reverse('galaxyzoo:pattern', args=(1,)))

def to_sa(request, question_id):

    return HttpResponseRedirect(reverse('galaxyzoo:sa', args=(1,)))

def to_sa_num(request, question_id):

    return HttpResponseRedirect(reverse('galaxyzoo:sa_num', args=(1,)))

def to_prominence(request, question_id):

    return HttpResponseRedirect(reverse('galaxyzoo:prominence', args=(1,)))

def to_tidal(request, question_id):

    return HttpResponseRedirect(reverse('galaxyzoo:tidal', args=(1,)))

def to_odd(request, question_id):

    return HttpResponseRedirect(reverse('galaxyzoo:odd', args=(1,)))





