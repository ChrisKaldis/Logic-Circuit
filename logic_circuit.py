from dimod import BinaryQuadraticModel, quicksum
from dimod.generators import and_gate, or_gate
from dwave.system import DWaveSampler, EmbeddingComposite


def format_input() -> str:
    """ Creates the binary representation of a single digit decimal number.    
    
        It gets an input from a user and checks if it is an integer that
        represents a single digit, after that it transforms the number 
        into a four digit binary number in order to describe the input of the 
        logic circuit.

        Returns:
            A string that represents a binary number with four digits.
    """

    while True:
        user_input = input("Select a single digit number:")

        try:
            user_input = int(user_input)
        except ValueError:
            print("Input type must be int")
            continue

        # The cqm is created by a bcd to 7 segment display decoder,
        # so input must be in range of a single digit decimal number.
        if user_input not in range(0, 10):
            print("Input must be an integer between [0,9]")
            continue

        binary_user_input = [i for i in bin(user_input)]
        # binary numbers starts with 0b in python
        digits_length = len(binary_user_input) - 2

        # In case number is not 8 or 9 it is represented in binary with
        # less than 4 digits so we add zeros in order to have a proper 
        # input in our gates that correspond to contraints.
        for _ in range(digits_length, 4):
            binary_user_input.insert(2, '0')
        binary_user_input = ''.join(binary_user_input)

        return binary_user_input

def a() -> BinaryQuadraticModel:
    bqm_gate1 = or_gate('A', 'C', 'out1')
    bqm_gate2 = and_gate('B', 'D', 'out2')
    bqm_gate3 = and_gate('B', 'D', 'out3')
    bqm_gate3.flip_variable('B')
    bqm_gate3.flip_variable('D')
    bqm_gate4 = or_gate('out2', 'out3', 'out4')
    bqm_gate5 = or_gate('out1', 'out4', 'a')

    bqm = bqm_gate1 + bqm_gate2 + bqm_gate3 + bqm_gate4 + bqm_gate5
    return bqm


def b() -> BinaryQuadraticModel:
    pass


def c() -> BinaryQuadraticModel:
    pass


def d() -> BinaryQuadraticModel:
    pass


def e() -> BinaryQuadraticModel:
    pass


def f() -> BinaryQuadraticModel:
    pass


def g() -> BinaryQuadraticModel:
    pass


def seven_segment_display_circuit() -> BinaryQuadraticModel:
    """Create the BQM of the circuit."""

    bqm_a = a()
    bqm_b = b()
    bqm_c = c()
    bqm_d = d()
    bqm_e = e()
    bqm_f = f()
    bqm_g = g()
    
    bqm = (bqm_a + bqm_b + bqm_c + bqm_d + bqm_e + bqm_f + bqm_g)
    return bqm


def format_output():
    """Represents basic information of the sampler's answer."""
    pass


def main():
    pass


if __name__ == '__main__':
    main()
