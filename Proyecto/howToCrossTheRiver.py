# Non-deterministic implementation to solve the problem "How to cross the river"
'''
The Puzzle:

A man has to get a fox, a chicken, and a sack of corn across a river.
He has a rowboat, and it can only carry him and one other thing.

If the fox and the chicken are left together, the fox will eat the chicken.
If the chicken and the corn are left together, the chicken will eat the corn.
How does the man do it?

'''

# Required libraries
import random

Far_Shore = []
Near_Shore = ['Farmer', 'Fox', 'Goose', 'Corn']
Path = []


def isValid(Shore):
  if ('Fox' in Shore and 'Goose' in Shore and len(Shore) == 2):
    return False
  if ('Goose' in Shore and 'Corn' in Shore and len(Shore) == 2):
    return False
  return True


def resetProblem():
  global Far_Shore, Near_Shore, Path
  Far_Shore = []
  Near_Shore = ['Farmer', 'Fox', 'Goose', 'Corn']
  Path = []


def boatPath(orig, dest):
  first_path = random.choice(orig)
  if (first_path != 'Farmer'):
    orig.remove(first_path)
    dest.append(first_path)
  orig.remove('Farmer')
  dest.append('Farmer')
  return (first_path, 'Farmer')


def HCR():
   orig = Near_Shore
   dest = Far_Shore

   while len(Far_Shore) != 4:
    first_path, second_path = boatPath(orig, dest)
    if isValid(orig) and isValid(dest):
      Path.append((first_path, second_path))
      orig, dest = dest, orig
    else:
      resetProblem()
      orig = Near_Shore
      dest = Far_Shore
   return Path

def optimal_solution():
  global Far_Shore, Near_Shore, Path
  path = HCR()
  while len(path) > 7:    
    resetProblem()
    path = HCR()
  return path