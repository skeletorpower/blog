from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from urllib.parse import quote_plus

from urllib3.request import urlencode

from django.core.paginator import Paginator
from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post


from .forms import PostForm
# Create your views here.

def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        #message here
        messages.success(request, 'Successifully created!')
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        'form': form,
    }

    return render(request, 'post_form.html', context)



def post_list(request):

    queryset_list = Post.objects.all()#.order_by("-timestamp")
    paginator = Paginator(queryset_list, 10)  # Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    queryset = paginator.get_page(page)

    context = {
        'object_list': queryset,
        'title': 'List',
        'page_request_var': page_request_var,

    }

    return render(request, 'post_list.html', context)

# def listing(request):
#     contact_list = Contacts.objects.all()
#
#     return render(request, 'list.html', {'contacts': contacts})
#



def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    share_string = quote_plus(instance.content)
    context = {
        'title': instance.title,
        'instance': instance,
        'share_string': share_string,

    }

    return render(request, 'post_detail.html', context)

def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        #message of success
        messages.success(request, 'Successifully updated!')
        return HttpResponseRedirect(instance.get_absolute_url())
    # else:
    #     messages.error(request, 'Error while updating...')

    context = {
        'title': instance.title,
        'instance': instance,
        'form': form,

    }

    return render(request, 'post_form.html', context)

def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, 'Item deleted!')
    return redirect('list')
