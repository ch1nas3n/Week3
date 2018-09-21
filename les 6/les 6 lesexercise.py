name = 'Julie'

def hallo(name):
   line = 'Welcome, ' + name + ', to the world of Pyhton.'
   print(line)

hallo('Julie')

lijst = ([4, 0, 1, -2])

def rng(lst):
    res = (max(lst) - min(lst))
    return res

rng(lijst)