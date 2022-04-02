import unittest

# from tests.examples.d_repetition import     tests_repetition
# suite = unittest.TestLoader().loadTestsFromModule(tests_repetition)

#from tests.examples.b_input_process_output import tests_input_process_output
#from tests.examples.e_functions import tests_functions
from tests.homework.h_strings import tests_strings
#from tests.examples.g_lists_and_tuples import tests_lists_and_tuples

suite = unittest.TestLoader().loadTestsFromModule(tests_strings)

unittest.TextTestRunner(verbosity=2).run(suite)