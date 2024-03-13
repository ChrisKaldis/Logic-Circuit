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


def a_logic_circuit() -> BinaryQuadraticModel:
    bqm_gate1 = or_gate('A', 'C', 'out1')
    bqm_gate2 = and_gate('B', 'D', 'out2')
    bqm_gate3 = and_gate('B', 'D', 'out3')
    bqm_gate3.flip_variable('B')
    bqm_gate3.flip_variable('D')
    bqm_gate4 = or_gate('out2', 'out3', 'out4')
    bqm_gate5 = or_gate('out1', 'out4', 'a')

    gates = [bqm_gate1, bqm_gate2, bqm_gate3, bqm_gate4, bqm_gate5]
    return quicksum(gates)


def b_logic_circuit() -> BinaryQuadraticModel:
    bqm_gate1 = and_gate('C', 'D', 'out6')
    bqm_gate2 = and_gate('C', 'D', 'out7')
    bqm_gate2.flip_variable('C')
    bqm_gate2.flip_variable('D')
    bqm_gate3 = or_gate('B', 'out6', 'out8')
    bqm_gate3.flip_variable('B')
    bqm_gate4 = or_gate('out7', 'out8', 'b')

    gates = [bqm_gate1, bqm_gate2, bqm_gate3, bqm_gate4]
    return quicksum(gates)


def c_logic_circuit() -> BinaryQuadraticModel:
    bqm_gate1 = or_gate('B', 'C', 'out10')
    bqm_gate1.flip_variable('C')
    bqm_gate2 = or_gate('D', 'out10', 'c')

    gates = [bqm_gate1, bqm_gate2]
    return quicksum(gates)


def d_logic_circuit() -> BinaryQuadraticModel:
    bqm_gate1 = and_gate('B', 'D', 'out12')
    bqm_gate1.flip_variable('B')
    bqm_gate1.flip_variable('D')
    bqm_gate2 = and_gate('B', 'C', 'out13')
    bqm_gate2.flip_variable('B')
    bqm_gate3 = and_gate('B', 'C', 'out14')
    bqm_gate3.flip_variable('C')
    bqm_gate4 = and_gate('C', 'D', 'out15')
    bqm_gate4.flip_variable('D')
    bqm_gate5 = or_gate('out12', 'out13', 'out16')
    bqm_gate6 = and_gate('D', 'out14', 'out17')
    bqm_gate7 = or_gate('out15', 'out17', 'out19')
    bqm_gate8 = or_gate('A', 'out16', 'out18')
    bqm_gate9 = or_gate('out18', 'out19', 'd')

    gates = [
        bqm_gate1, bqm_gate2, bqm_gate3, bqm_gate4, bqm_gate5, 
        bqm_gate6, bqm_gate7, bqm_gate8, bqm_gate9
        ]
    return quicksum(gates)


def e_logic_circuit() -> BinaryQuadraticModel:
    bqm_gate1 = and_gate('B', 'D', 'out21')
    bqm_gate1.flip_variable('B')
    bqm_gate1.flip_variable('D')
    bqm_gate2 = and_gate('C', 'D', 'out22')
    bqm_gate2.flip_variable('D')
    bqm_gate3 = or_gate('out21', 'out22', 'e')

    gates = [bqm_gate1, bqm_gate2, bqm_gate3]
    return quicksum(gates)


def f_logic_circuit() -> BinaryQuadraticModel:
    bqm_gate1 = and_gate('C', 'D', 'out24')
    bqm_gate1.flip_variable('C')
    bqm_gate1.flip_variable('D')
    bqm_gate2 = and_gate('B', 'C', 'out25')
    bqm_gate2.flip_variable('C')
    bqm_gate3 = and_gate('B', 'D', 'out26')
    bqm_gate3.flip_variable('D')
    bqm_gate4 = or_gate('A', 'out26', 'out27')
    bqm_gate5 = or_gate('out27', 'out25', 'out28')
    bqm_gate6 = or_gate('out28', 'out24', 'f')

    gates = [bqm_gate1, bqm_gate2, bqm_gate3, bqm_gate4, bqm_gate5, bqm_gate6]
    return quicksum(gates)


def g_logic_circuit() -> BinaryQuadraticModel:
    bqm_gate1 = and_gate('B', 'C', 'out30')
    bqm_gate1.flip_variable('C')
    bqm_gate2 = and_gate('C', 'D', 'out31')
    bqm_gate2.flip_variable('D')
    bqm_gate3 = and_gate('B', 'C', 'out32')
    bqm_gate3.flip_variable('B')
    bqm_gate4 = or_gate('out30', 'out31', 'out33')
    bqm_gate5 = or_gate('A', 'out32', 'out34')
    bqm_gate6 = or_gate('out33', 'out34', 'g')

    gates = [bqm_gate1, bqm_gate2, bqm_gate3, bqm_gate4, bqm_gate5, bqm_gate6]
    return quicksum(gates)


def seven_segment_display_circuit(input_signal: str) -> BinaryQuadraticModel:
    """Create the BQM of the circuit."""

    # creates a list with the values of the input in 4 binary values.
    signal = [int(digit) for i, digit in enumerate(input_signal) if i > 1]
    bqm = [
        a_logic_circuit(), b_logic_circuit(), c_logic_circuit(), d_logic_circuit(),
        e_logic_circuit(), f_logic_circuit(), g_logic_circuit()
    ]
    bqm = quicksum(bqm)
    bqm.fix_variables(
        [('A', signal[0]), ('B', signal[1]), ('C', signal[2]), ('D', signal[3])]
    )
    return bqm


def format_output():
    """Represents basic information of the sampler's answer."""
    pass


def main():
    pass


if __name__ == '__main__':
    main()
