from django.shortcuts import render
from django.http import HttpResponse

projectList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'Fully functional Portfolio website'
    },
    {
        'id': '3',
        'title': 'Social Network Website',
        'description': 'Fully functional Social Network website'
    },

]


def projects(request):
    context = {
        'projects': projectList
    }
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projObj = None
    for i in projectList:
        if i['id'] == pk:
            projObj = i
    return render(request, 'projects/single-project.html', {'project': projObj})
