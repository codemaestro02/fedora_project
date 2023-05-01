from django.db.models import Q
from django.shortcuts import render

from .models import Question

# Create your views here.

def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')

def search(request):
    keywords = ''

    if request.method == 'GET': # form was submitted

        keywords = request.GET.get("contact-question", "")  # <input type="text" name="keywords">
        all_queries = None
        search_fields = ('question_text', 'answer_text')  # change accordingly
        for keyword in keywords.split(' '):  # keywords are splitted into words (eg: john science library)
            keyword_query = None
            for field in search_fields:
                each_query = Q(**{field + '__icontains': keyword})
                if not keyword_query:
                    keyword_query = each_query
                else:
                    keyword_query = keyword_query | each_query
                    if not all_queries:
                        all_queries = keyword_query
                    else:
                        all_queries = all_queries & keyword_query

        faqs = Question.objects.filter(all_queries).distinct()
        context = {'faqs': faqs}
        return render(request, 'main/contact.html', context)
    else:  # no data submitted
        context = {}
        return render(request, 'main/contact.html', context)

def contact(request):
    faqs = Question.objects.all()
    context = {
        "faqs": faqs,
    }
    return render(request, 'main/contact.html', context)