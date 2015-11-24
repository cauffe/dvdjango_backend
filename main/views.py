from django.shortcuts import render, render_to_response
from django.template import RequestContext

from django.http import JsonResponse
from main.models import Movie, MovieCas
from django.views.generic import ListView

from django.core.paginator import Paginator, InvalidPage, EmptyPage

import string
# Create your views here.


def movie_list_dbv(request):  
    context = {}

    movie_list = Movie.objects.all()[:100]

    paginator = Paginator(movie_list, 10)

    page = request.GET.get('page', '1')

    # page = request.GET['page']

    try:
        movie_list = paginator.page(page)
    except (InvalidPage, EmptyPage):
        movie_list = paginator.page(paginator.num_pages)

    context['movie_list'] = movie_list

    return render_to_response('movie_list_dbv.html',context, context_instance=RequestContext(request))


class MovieListView(ListView):  
    model = Movie
    queryset = Movie.objects.all()[:100]
    template_name = "movie_list_cbv.html"
    context_object_name = "movie_list"

def movie_list(request):

    page = request.GET.get('page', '1')
    letter = request.GET.get('letter', 'A')

    movies = Movie.objects.filter(title__istartswith=letter)

    paginator = Paginator(movies, 10)

    try:
        movies = paginator.page(page)
    except (InvalidPage, EmptyPage):
        movies = paginator.page(paginator.num_pages)  

    api_dict = {}

    movie_list = []

    api_dict['movies'] = movie_list


    for movie in movies:
        movie_list.append({'title': movie.title,
                           'release': movie.release,
                           'pk': movie.pk,
                           })

    try:
        api_dict['next_page'] = movies.next_page_number()
    except:
        pass

    try:
        api_dict['previous_page'] = movies.previous_page_number()
    except:
        pass

    api_dict['current_page'] = movies.number

    api_dict['all_pages'] = movies.paginator.num_pages


    api_dict['letters'] = list(string.ascii_uppercase)

    return JsonResponse(api_dict)

def movie_detail(request, pk):

    movie = Movie.objects.get(pk=pk)

    movie_detail = {'title': movie.title,
                    'price': movie.price,
                    'rating': movie.rating,
                    'release': movie.release,
                    }

    return JsonResponse(movie_detail)
