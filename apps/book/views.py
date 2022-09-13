from operator import attrgetter

from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View

from .forms import BookForm
from .models import BookData
from django.views.generic import ListView, CreateView, DeleteView, UpdateView


# Create your views here.


class BookView(ListView):
    model = BookData
    template_name = 'book/book_list.html'
    context_object_name = 'book_data'


class BookAdd(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': BookForm()}
        return render(request, 'book/book_add.html', context)

    def post(self, request, *args, **kwargs):
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            BookData.save(book)
            return redirect('listing')
        return render(request, 'book/book_add.html', {'form': form})


class BookUpdateView(View):
    def edit_book(request, id):
        student_obj = BookData.objects.get(pk=id)
        form = BookForm(instance=student_obj)
        if request.method == "POST":
            form = BookForm(request.POST, instance=student_obj)
            if form.is_valid():
                form.save()
                return redirect("listing")
        else:
            context = {"form": form}
        return render(request, 'book/bookdata_update_form.html', context)

    def delete_book(request, id):
        book_delete = BookData.objects.get(pk=id)
        book_delete.delete()
        messages.error(request, ("You have deteted book data succussfully! "))
        return render(request, 'book/book_delete.html', {"book_delete": book_delete})


class BookSearch(View):
    def stud_queryset(query=None):
        queryset = []
        queries = query.split(" ")
        for q in queries:
            book_search = BookData.objects.filter(
                Q(name__startswith=q)
            ).distinct()
            for st in book_search:
                queryset.append(st)
        return list(set(queryset))

    def Search(request, *args, **kwrgs):
        context = {}
        query = ""
        if request.GET:
            query = request.GET.get('q', '')
            context['query'] = str(query)
        book_search = sorted(BookSearch.stud_queryset(query), key=attrgetter('name'))
        # Pagination
        page = request.GET.get('page', 1)
        post_paginator = Paginator(book_search, 4)
        try:
            book_search = post_paginator.page(page)
        except PageNotAnInteger:
            book_search = post_paginator.page(4)
        except EmptyPage:
            book_search = post_paginator.page(post_paginator.num_pages)

        context['book_search'] = book_search
        # search = request.GET["query"]
        # Stud_search = Student.objects.filter(full_name__startswith= search)
        return render(request, 'student_search.html', context)
