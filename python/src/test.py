import cProfile
import re

def  my_func():
    for i in range(100):
        re.match('a', 'a')

cProfile.run('my_func()')
