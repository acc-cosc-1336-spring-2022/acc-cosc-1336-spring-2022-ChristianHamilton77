import unittest

# from tests.examples.d_repetition import     tests_repetition
# suite = unittest.TestLoader().loadTestsFromModule(tests_repetition)

#from tests.examples.b_input_process_output import tests_input_process_output
from tests.homework.d_repetition import tests_repetition      
suite = unittest.TestLoader().loadTestsFromModule(tests_repetition)

unittest.TextTestRunner(verbosity=2).run(suite)