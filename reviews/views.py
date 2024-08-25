from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect

from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

# Create your views here.


class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thanks-you"

    
'''    
def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks-you')
    else:
        form = ReviewForm()
    review = Review.objects.all()
    print(review)
    return render(request, "reviews/review.html", {
        "form":form
    })
'''

class ThankYouView(TemplateView):
    template_name = "reviews/thanks-you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This Works!"
        return context


#def thanks_you(request):
#    return render(request, "reviews/thanks-you.html")


class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    #def get_queryset(self) -> QuerySet[Any]:
     #   base = super().get_queryset()
      #  data = base.filter(rating__gt=3)
       # return data
    


class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review
