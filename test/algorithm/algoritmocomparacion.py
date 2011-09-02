from bzrlib.patiencediff import unified_diff
from bzrlib.patiencediff import PatienceSequenceMatcher
from difflib import Differ
import sys

__author__ = 'nenopera'

text1 = '''  1. Beautiful is better than ugly.
  2. Explicit is better than implicit.
  3. Simple is better than complex.
  4. Complex is better than complicated.
  
  function hola {
    if (true) {
        print "adios"
    }
  }

  function eco {
    if (true) {
        yyy = 98
    } else {
        cant = 45 + 3
    }
  }
'''.splitlines(1)

text2 = '''  1. Beautiful is better than ugly.
  3.   Simple is better than complex.
  4. Complicated is better than complex.
  5. Flat is better than nested.

  function hola {
    if (true) {
        print "adios"
    }
  }

  function adios {
    while (true) {
        switch a:
            case
            print "aaaa"*4
            break
    }
  }

  function eco {
    if (true) {
        yyy = 98
    } else {
        cant = 45 + 3
    }
  }
'''.splitlines(1)

d = Differ()

def print_line(message):
    print
    print message + " " + "-" * 20
    print

print_line("texto1")

sys.stdout.writelines(text1)

print_line("texto2")

sys.stdout.writelines(text2)

print_line("comparacion normal texto1 a texto2")

sys.stdout.writelines(list(d.compare(text1, text2)))

print_line("comparacion normal texto2 a texto1")

sys.stdout.writelines(list(d.compare(text2, text1)))

matcher = PatienceSequenceMatcher

print_line("comparacion PATTIENCE texto1 a texto2")

sys.stdout.writelines(list(unified_diff(text1, text2,
                        fromfile="texto1", tofile="texto2",
                        sequencematcher=matcher)))

print_line("comparacion PATTIENCE texto2 a texto1")

sys.stdout.writelines(list(unified_diff(text2, text1,
                        fromfile="texto2", tofile="texto1",
                        sequencematcher=matcher)))