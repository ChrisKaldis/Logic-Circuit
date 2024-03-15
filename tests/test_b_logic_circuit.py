import unittest

from dimod import ExactSolver, keep_variables

from logic_circuit import b_logic_circuit


class TestLogicCircitB(unittest.TestCase):

    def test_b_logic_circuit(self):
        bqm_b = b_logic_circuit()
        solver = ExactSolver()
        samples = solver.sample(bqm_b)
        samples_low_energy = keep_variables(
            samples, ['B', 'C', 'D', 'b']
        ).lowest()
        
        for samples in samples_low_energy:
            input_value = ''.join(
                [str(samples['B']), str(samples['C']), str(samples['D'])]
            )
            if input_value == '101' or input_value == '110':
                self.assertEqual(samples['b'], 0)
            else:
                self.assertEqual(samples['b'], 1)


if __name__ == '__main__':
    unittest.main()