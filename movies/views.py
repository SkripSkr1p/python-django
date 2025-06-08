from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Movie, Review
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin
from django.urls import reverse_lazy, reverse
from django.views.decorators.http import require_POST
from .forms import CreateReviewForm
from django.shortcuts import redirect

class MoviesView(ListView):
    model = Movie
    paginate_by = 10
    template_name = "movies/index.html"


# LoginRequiredMixin
class MovieView(FormMixin,DetailView):
    form_class = CreateReviewForm
    model = Movie
    template_name = 'movies/detail.html'



class NewMovie(CreateView):
    model = Movie
    template_name = 'movies/CreateMovies.html'
    fields = ["title", "filmed", "duration", "slug"]
    success_url = reverse_lazy('movies')

    

class UpdateMovie(UpdateView):
    model = Movie
    template_name = 'movies/UpdateMovie.html'
    fields = ["title", "filmed", "duration", "slug"]


    def get_success_url(self):
        return reverse('movie', kwargs={'slug': self.object.slug})
    
class DeleteMovie(DeleteView):
    model = Movie
    template_name = 'movies/DeleteMovie.html'
    success_url = reverse_lazy('movies')
    

@login_required
@require_POST
def add_review(request, slug):
    movie = Movie.objects.filter(slug=slug)[0]
    new_review_form = CreateReviewForm(request.POST)
    if new_review_form.is_valid():
        content = new_review_form.cleaned_data['content']
        new_review = Review(content=content, movie=movie, author=request.user)
        new_review.save() # TODO
    return redirect('movie', slug=slug)