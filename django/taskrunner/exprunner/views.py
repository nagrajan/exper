# Create your views here.
from django.shortcuts import HttpResponse
from exprunner import startNewTask
from models import Experiment

def viewStatus(request):
    objs = Experiment.objects.all()
    statuses = [str((o.pk, o.name, o.status)) for o in objs]
    statuses = '\n'.join(statuses)
    status = "<pre>" + statuses + "</pre>"
    return HttpResponse("in view status method\n%s"%status)

def addTask(request, taskinfo):
    rv = startNewTask(taskinfo)
    if rv is not None:
        return HttpResponse(rv)
    return HttpResponse("Failed to start task")

def home(request):
    response = """
    <html>
      <body>
        <h2> Welcome to the home page </h2>
        <p> Nothing here though </p>
        <p> However, you can add tasks using <a href="/addtask">asstask</a> and <a href="/status">view status</a> page. </p>
      </body>
    </html>
    """
    return HttpResponse(response)



