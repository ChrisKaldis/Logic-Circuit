import unittest

from dimod import ExactSolver, keep_variables

from logic_circuit import e_logic_circuit


class TestLogicCircitE(unittest.TestCase):

    def test_e_logic_circuit(self):
        bqm_e = e_logic_circuit()
        solver = ExactSolver()
        samples = solver.sample(bqm_e)
        samples_low_energy = keep_variables(samples, ['B', 'C', 'D', 'e']).lowest()
        
        for samples in samples_low_energy:
            input_value = ''.join(
                [str(samples['B']), str(samples['C']), str(samples['D'])]
            )
            if (input_value == '000' or input_value == '010' or 
                input_value == '110'):
                self.assertEqual(samples['e'], 1)
            else:
                self.assertEqual(samples['e'], 0)


if __name__ == '__main__':
    unittest.main()