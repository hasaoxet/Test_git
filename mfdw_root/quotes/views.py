from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Quote
from .forms import QuoteForm
from pages.models import Page #tại sao lại cần cái này? nhìn vào cái return ở dưới kia kìa

def quote_req(request):
    submitted = False
    if request.method == 'POST':
        form = QuoteForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()  # lưu form và db chăng???
            return HttpResponseRedirect('/quote/?submitted=True')
    else:
        form = QuoteForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request,'quote.html', {'form':form, 'page_list':Page.objects.all(),'submitted':submitted})

class QuoteList(ListView):
    model = Quote
    context_object_name = 'all_quotes'
    template_name = 'quote_list.html'

    def get_context_data(self, **kwargs):
        context = super(QuoteList,self).get_context_data(**kwargs)
        context['page_list']=Page.objects.all()
        return context

class QuoteView(DetailView):
    model = Quote
    context_object_name = 'quote'
    template_name = 'quote_detail.html'

    def get_context_data(self, **kwargs):
        context = super(QuoteView,self).get_context_data(**kwargs)
        context['page_list']=Page.objects.all()
        return context