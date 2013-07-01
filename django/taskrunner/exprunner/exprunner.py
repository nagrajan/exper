from thread import start_new_thread
from subprocess import Popen, PIPE, STDOUT
from threading import Lock
dbUpdateLock = Lock()
from models import Experiment

import os

def updateTaskInDb(name, status, pk=None):
    # acquire lock
    dbUpdateLock.acquire()
    try:
        # check if entry in db
        if pk is None:
            # if not in db, make new one
            ne = Experiment(name=name, status=status)
            ne.save()
            pk = ne.pk

        else:
            # if present, retrieve and update it
            ne = Experiment.objects.get(pk=pk)
            ne.status = status
            ne.save()
            pk = ne.pk
    except:
        print "Error in updating database entry"
        pk = None
    finally:
        dbUpdateLock.release()
    return pk


def startNewTask(taskinfo):
    pk = updateTaskInDb(taskinfo, 'added to queue')
    if pk is not None:
        start_new_thread(runAndMonitorTask, (taskinfo, pk))
        return "Task id %s started"%str(pk)
    return None


def getParentDir(path, level=None):
    if level is None:
        level = 1

    while level > 0:
        level -= 1
        path = os.path.dirname(path)
    return path

def runAndMonitorTask(taskinfo, pk):
    p = Popen(['/usr/bin/python', os.path.join(getParentDir(__file__, 1), 'runExternalTask.py')], stdout=PIPE, stderr=PIPE)
    data1 = [line for line in p.stdout.readlines()]
    data2 = p.stderr.read()
    print data1
    print data2
    retval = p.wait()
    updateTaskInDb(taskinfo, "task funished running with exit code %s"%retval, pk)
    pass


