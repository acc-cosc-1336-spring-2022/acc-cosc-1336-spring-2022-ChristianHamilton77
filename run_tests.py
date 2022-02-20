import unittest

from tests.homework.c_decisions import tests_decisions
suite = unittest.TestLoader().loadTestsFromModule(tests_decisions)

#from tests.examples.b_input_process_output import tests_input_process_output
#from tests.examples.d_repetition import tests_repetition      
# suite = unittest.TestLoader().loadTestsFromModule(tests_repetition)

unittest.TextTestRunner(verbosity=2).run(suite)