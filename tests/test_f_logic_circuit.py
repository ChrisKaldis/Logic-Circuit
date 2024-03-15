import unittest

from dimod import ExactSolver, keep_variables

from logic_circuit import f_logic_circuit


class TestLogicCircitF(unittest.TestCase):

    def test_f_logic_circuit(self):
        bqm_f = f_logic_circuit()
        solver = ExactSolver()
        samples = solver.sample(bqm_f)
        samples_low_energy = keep_variables(
            samples, ['A', 'B', 'C', 'D', 'f']
        ).lowest()
        
        for samples in samples_low_energy:
            input_value = ''.join(
                [str(samples['A']), str(samples['B']), 
                 str(samples['C']), str(samples['D'])]
            )
            if (input_value == '0001' or input_value == '0010' or 
                input_value == '0011' or input_value == '0111'):
                self.assertEqual(samples['f'], 0)
            else:
                self.assertEqual(samples['f'], 1)


if __name__ == '__main__':
    unittest.main()