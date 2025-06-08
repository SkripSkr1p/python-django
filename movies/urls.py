from django.urls import path

from .views import MoviesView, MovieView, NewMovie, UpdateMovie, DeleteMovie, add_review

urlpatterns = [
    path("", MoviesView.as_view(), name="movies"),
    path("new", NewMovie.as_view(), name="movie_new"),
    path("<str:slug>", MovieView.as_view(), name="movie"),
    path("delete/<str:slug>", DeleteMovie.as_view(), name="movie_delete"),
    path("update/<str:slug>", UpdateMovie.as_view(), name="movie_update"),
    path("<str:slug>/add_review", add_review, name='add_review')
]
