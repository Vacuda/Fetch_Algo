from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, 'pyramid/index.html')



    # def edit_project(request, project_id):
    # context = {
    #     "project": Project.objects.filter(id=project_id)[0],
    # }
    # return render(request, 'project_app/project_edit_page.html', context)