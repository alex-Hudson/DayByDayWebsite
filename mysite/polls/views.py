from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, PassageTitle, Series


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_series_list'

    def get_queryset(self):
        """
        Return the last five published series (not including those set to be
        published in the future).
        """
        return Series.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = PassageTitle
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any passage_titles that aren't published yet.
        """
        return PassageTitle.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = PassageTitle
    template_name = 'polls/results.html'


def vote(request, passage_title_id):
    passage_title = get_object_or_404(PassageTitle, pk=passage_title_id)
    try:
        selected_passage_text_and_question = passage_title.passage_text_and_questions_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the passage title.
        return render(request, 'polls/detail.html', {
            'passage_title': passage_title,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_passage_text_and_question.votes += 1
        selected_passage_text_and_question.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(passage_title.id,)))
