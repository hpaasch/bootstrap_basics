from django.shortcuts import render

from scotus_app.models import SupremeCourtJustice


def homepage_view(request):
    return render(request, 'homepage.html', {})


def court_view(request):
    context = {
        'justices': SupremeCourtJustice.objects.all()
    }
    return render(request, 'court.html', context)


def about_view(request):
    return render(request, 'about.html', {})


def women_view(request):
    context = {
        'justices': SupremeCourtJustice.objects.filter(gender__exact='F'),
        'total': SupremeCourtJustice.objects.filter(gender__exact='F').count(),
    }
    return render(request, 'women.html', context)


def men_view(request):
    context = {
        'justices': SupremeCourtJustice.objects.filter(gender__exact='M'),
        'total': SupremeCourtJustice.objects.filter(gender__exact='M').count(),
    }
    return render(request, 'men.html', context)
