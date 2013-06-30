print "this is printed by the external task and caught by the django thread."

print "this task sleeps for 15 seconds simulating an external task. Sleeping now..."
from time import sleep
sleep(15)

print "external task wakes up and ends"