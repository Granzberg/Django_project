from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Comment
from .forms import RegistrationUser, SearchForm, CommentForm
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from django.views.generic.detail import DetailView

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


class Products(TemplateView):
    extra_context = {'form': SearchForm}
    template_name = 'product_list.html'
    context_object_name = 'categories', 'product'
    model = Category

    def get_context_data(self, **kwargs):
        context = super(Products, self).get_context_data(**kwargs)
        context.update({
            'categories': Category.objects.order_by('name'),
            'products': Product.objects.order_by('name'),
        })
        return context

    def post(self, request):
        print(request.POST)


class HomePageView(TemplateView):
    template_name = 'base.html'


class SearchResultsView(ListView):
    model = Product
    template_name = 'search_page.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(
            Q(name__icontains=query)
        )
        return object_list


class ProductsView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

    def post(self, request):
        print(request.POST)


def detail_product(request, pk):
    post = get_object_or_404(Product, pk=pk)
    comments = post.comments.filter(activate=True)
    print(comments)
    if request.method == 'POST':

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = Comment(
                name=comment_form.cleaned_data['name'],
                email=comment_form.cleaned_data['email'],
                body=comment_form.cleaned_data['body'],
                post=post
            )
            new_comment.post = post
            new_comment.save()
        else:
            comment_form.errors()
    else:
        comment_form = CommentForm()

    return render(request, 'product_detail.html', context={'product': post, 'post': post, 'comments': comments,
                                                           'comment_form': comment_form})


#def LoginView(request):
    # username = request.POST['username']
    # password = request.POST['password']
    # user = authenticate(request, username=username, password=password)
    # if user is not None:
    #     login(request, user)
    #     # Redirect to a success page.
    #     ...
    # else:
    #     # Return an 'invalid login' error message.
    #     ...

