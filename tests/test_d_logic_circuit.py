import unittest

from dimod import ExactSolver, keep_variables

from logic_circuit import d_logic_circuit


class TestLogicCircitD(unittest.TestCase):

    def test_d_logic_circuit(self):
        bqm_d = d_logic_circuit()
        solver = ExactSolver()
        samples = solver.sample(bqm_d)
        samples_low_energy = keep_variables(
            samples, ['A', 'B', 'C', 'D', 'd']
        ).lowest()
        
        for samples in samples_low_energy:
            input_value = ''.join(
                [str(samples['A']), str(samples['B']), 
                 str(samples['C']), str(samples['D'])]
            )
            if (input_value == '0001' or input_value == '0100' or 
                input_value == '0111'):
                self.assertEqual(samples['d'], 0)
            else:
                self.assertEqual(samples['d'], 1)


if __name__ == '__main__':
    unittest.main()