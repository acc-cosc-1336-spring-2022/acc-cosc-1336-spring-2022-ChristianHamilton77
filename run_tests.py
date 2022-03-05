import unittest

# from tests.examples.d_repetition import     tests_repetition
# suite = unittest.TestLoader().loadTestsFromModule(tests_repetition)

#from tests.examples.b_input_process_output import tests_input_process_output
from tests.homework.e_functions import tests_functions
suite = unittest.TestLoader().loadTestsFromModule(tests_functions)

unittest.TextTestRunner(verbosity=2).run(suite)