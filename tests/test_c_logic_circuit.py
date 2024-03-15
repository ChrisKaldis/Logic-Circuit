import unittest

from dimod import ExactSolver, keep_variables

from logic_circuit import c_logic_circuit


class TestLogicCircitC(unittest.TestCase):

    def test_c_logic_circuit(self):
        bqm_c = c_logic_circuit()
        solver = ExactSolver()
        samples = solver.sample(bqm_c)
        samples_low_energy = keep_variables(
            samples, ['B', 'C', 'D', 'c']
        ).lowest()
        
        for samples in samples_low_energy:
            input_value = ''.join(
                [str(samples['B']), str(samples['C']), str(samples['D'])]
            )
            if input_value == '010':
                self.assertEqual(samples['c'], 0)
            else:
                self.assertEqual(samples['c'], 1)


if __name__ == '__main__':
    unittest.main()