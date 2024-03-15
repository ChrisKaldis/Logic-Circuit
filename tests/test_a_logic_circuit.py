import unittest

from dimod import ExactSolver, keep_variables

from logic_circuit import a_logic_circuit


class TestLogicCircitA(unittest.TestCase):

    def test_a_logic_circuit(self):
        bqm_a = a_logic_circuit()
        solver = ExactSolver()
        samples = solver.sample(bqm_a)
        samples_low_energy = keep_variables(
            samples, ['A', 'B', 'C', 'D', 'a']
        ).lowest()

        for samples in samples_low_energy:
            input_value = ''.join(
                [str(samples['A']), str(samples['B']), 
                 str(samples['C']), str(samples['D'])]
            )
            if input_value == '0001' or input_value == '0100':
                self.assertEqual(samples['a'], 0)
            else:
                self.assertEqual(samples['a'], 1)


if __name__ == '__main__':
    unittest.main()
