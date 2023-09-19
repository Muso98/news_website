from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView

from .models import News, Category
from .forms import ContactForm

def news_list(request):
    #news_list = News.objects.filter(status=News.Status.Published)
    news_list = News.published.all()
    context = {
        "news_list": news_list
    }
    return render(request, "news/news_list.html", context)

def news_detail(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published)
    context = {
        "news":news
    }
    return render(request, "news/news_detail.html", context)

# def homePageView(request):
#     categories = Category.objects.all()
#     news_list = News.published.all().order_by("-publish_time")[:5]
#     mahalliy_one = News.published.filter(category__name="Mahalliy").order_by("-publish_time")[0]
#     mahalliy_news = News.published.all().filter(category__name="Mahalliy").order_by("-publish_time")[1:6]
#     context = {
#         "news_list": news_list,
#         "categories": categories,
#         "mahalliy_one": mahalliy_one,
#         "mahalliy_news":mahalliy_news,
#     }
#
#     return render(request, "news/index.html", context)

class HomePageView(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['news_list']= News.published.all().order_by("-publish_time")[:4]
        context['mahalliy_news']= News.published.all().filter(category__name="Mahalliy").order_by("-publish_time")[:5]
        context['global_news'] = News.published.all().filter(category__name="Xorij").order_by("-publish_time")[:5]
        context['techno_news'] = News.published.all().filter(category__name="Texnalogiya").order_by("-publish_time")[:5]
        context['sport_news'] = News.published.all().filter(category__name="Sport").order_by("-publish_time")[:5]


        return context


# def contactPageView(request):
#     form = ContactForm(request.POST or None)
#     if request.method == "POST" and form.is_valid():
#         form.save()
#         return HttpResponse("<h2>Biz bilan bog'langaniz uchun tashakkur</h2>")
#
#     context = {
#         "form":form,
#     }
#     return render(request, "news/contact.html", context)


class ContactPageView(TemplateView):
    template_name = "news/contact.html"

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            "form":form
        }
        return render(request, "news/contact.html", context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == "POST" and form.is_valid():
            form.save()
            return HttpResponse("<h2>Biz bilan bog'langaniz uchun tashakkur</h2>")

        context = {
          "form":form,
        }
        return render(request, "news/contact.html", context)



def errorPageView(request):
    context = {

    }
    return render(request, "news/404.html", context)

class LocalNewsView(ListView):
    model = News
    template_name = "news/mahalliy.html"
    context_object_name = "mahalliy_yangiliklar"

    # def get_queryset(self):
    #     news = self.model.published.all().filter(category__name="Mahalliy")[:5]
    #     return news
    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['mahalliy_yangiliklar']= News.published.all().filter(category__name="Mahalliy").order_by("-publish_time")[:5]
        context['tavsiya_mahalliy']= News.published.all().filter(category__name="Mahalliy").order_by("-publish_time")

        return context



class ForeignNewsView(ListView):
    model = News
    template_name = "news/xorij.html"
    context_object_name = "xorij_yangiliklar"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['xorij_yangiliklar'] = News.published.all().filter(category__name="Xorij").order_by("-publish_time")[:5]
        context['tavsiya_xorij'] = News.published.all().filter(category__name="Xorij").order_by("-publish_time")

        return context


class TechnologyNewsView(ListView):
    model = News
    template_name = "news/texnalogiya.html"
    context_object_name = "texnalogiya_yangiliklar"

    # def get_queryset(self):
    #     news = self.model.published.all().filter(category__name="Texnalogiya")
    #     return news

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['texnalogiya_yangiliklar'] = News.published.all().filter(category__name="Texnalogiya").order_by("-publish_time")[:5]
        context['tavsiya_texnalogiya'] = News.published.all().filter(category__name="Texnalogiya").order_by("-publish_time")

        return context

class SportNewsView(ListView):
    model = News
    template_name = "news/sport.html"
    context_object_name = "sport_yangiliklar"

    # def get_queryset(self):
    #     news = self.model.published.all().filter(category__name="Sport")
    #     return news

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sport_yangiliklar'] = News.published.all().filter(category__name="Sport").order_by("-publish_time")[:5]
        context['tavsiya_sport'] = News.published.all().filter(category__name="Sport").order_by("-publish_time")

        return context