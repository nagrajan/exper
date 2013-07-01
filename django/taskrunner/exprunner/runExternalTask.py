from sys import stderr
print "this is printed by the external task and caught by the django thread."

print "this task sleeps for 15 seconds simulating an external task. Sleeping now..."
from time import sleep
sleep(15)

print "external task wakes up and ends"

print >> stderr, "this message goes to stderr"

from random import randint
exit(randint(0,3))