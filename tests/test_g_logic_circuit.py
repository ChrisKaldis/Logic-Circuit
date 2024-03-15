import unittest

from dimod import ExactSolver, keep_variables

from logic_circuit import g_logic_circuit


class TestLogicCircitG(unittest.TestCase):

    def test_g_logic_circuit(self):
        bqm_g = g_logic_circuit()
        solver = ExactSolver()
        samples = solver.sample(bqm_g)
        samples_low_energy = keep_variables(
            samples, ['A', 'B', 'C', 'D', 'g']
        ).lowest()
        
        for samples in samples_low_energy:
            input_value = ''.join(
                [str(samples['A']), str(samples['B']), 
                 str(samples['C']), str(samples['D'])]
            )
            if (input_value == '0000' or input_value == '0001' or 
                input_value == '0111'):
                self.assertEqual(samples['g'], 0)
            else:
                self.assertEqual(samples['g'], 1)


if __name__ == '__main__':
    unittest.main()