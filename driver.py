__author__ = 'a1x'
from pyke import knowledge_engine, krb_traceback, goal
import sys
import time

# Compile and load .krb files in same directory that I'm in (recursively).
engine = knowledge_engine.engine(__file__)
fc_goal = goal.compile('parejas.render($person1, $person2, $relationship)')

def translate(text):
    if("_"in text):
        arrText = text.split('_')
        return  "%s='%s'"%(arrText[0],arrText[1])
    return ""

def test(pareja):
    engine.reset()
    start_time = time.time()
    engine.activate('relaciones')  # Runs all applicable forward-chaining rules.
    fc_end_time = time.time()
    fc_time = fc_end_time - start_time
    #print "doing proof"
    with fc_goal.prove(engine, person1=pareja) as gen:
        for vars, plan in gen:
            print "<%s %s > %s </%s>" % \
                    (pareja, translate(vars['person2']), vars['relationship'],pareja)
    prove_time = time.time() - fc_end_time
    #print
    #print "done"
    #engine.print_stats()

def header():
    strHTML = "<html>" \
              "<head><title>HTML Generator</title></head>" \
              "<body>"
    return strHTML

def footer():
    strHTML = "</body>" \
              "</html>"
    return strHTML