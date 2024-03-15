from dimod import BinaryQuadraticModel, SampleSet, quicksum, keep_variables
from dimod.generators import and_gate, or_gate
from dwave.system import DWaveSampler, EmbeddingComposite
from numpy import ndarray, zeros, savetxt


def format_input() -> str:
    """ Creates the binary representation of a single digit decimal number.    
    
        It gets an input from a user and checks if it is an integer that
        represents a single digit, after that it transforms the number 
        into a four digit binary number in order to describe the input of the 
        logic circuit.

        Returns:
            A string that represents a binary number in four digits.
    """
    while True:
        user_input = input('Select a single digit number:')
        try:
            user_input = int(user_input)
        except ValueError:
            print('Input type must be int')
            continue

        # The bqm is created by a bcd to 7 segment display decoder,
        # so input must be in range of a single digit decimal number.
        if user_input not in range(0, 10):
            print('Input must be an integer between [0,9]')
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
    """ a = A + C + BD + B'D'."""
    bqm_gate1 = or_gate('A', 'C', 'out1')
    bqm_gate2 = and_gate('B', 'D', 'out2')
    bqm_gate3 = and_gate('B', 'D', 'out3')
    bqm_gate3.flip_variable('B')
    bqm_gate3.flip_variable('D')
    bqm_gate4 = or_gate('out2', 'out3', 'out4')
    bqm_gate5 = or_gate('out1', 'out4', 'a')
    gates = quicksum([bqm_gate1, bqm_gate2, bqm_gate3, bqm_gate4, bqm_gate5])

    return gates


def b_logic_circuit() -> BinaryQuadraticModel:
    """ b = B' + C'D' + CD."""
    bqm_gate1 = and_gate('C', 'D', 'out6')
    bqm_gate2 = and_gate('C', 'D', 'out7')
    bqm_gate2.flip_variable('C')
    bqm_gate2.flip_variable('D')
    bqm_gate3 = or_gate('B', 'out6', 'out8')
    bqm_gate3.flip_variable('B')
    bqm_gate4 = or_gate('out7', 'out8', 'b')
    gates = quicksum([bqm_gate1, bqm_gate2, bqm_gate3, bqm_gate4])
    
    return gates


def c_logic_circuit() -> BinaryQuadraticModel:
    """ c = B + C' + D."""
    bqm_gate1 = or_gate('B', 'C', 'out10')
    bqm_gate1.flip_variable('C')
    bqm_gate2 = or_gate('D', 'out10', 'c')
    gates = quicksum([bqm_gate1, bqm_gate2])

    return gates


def d_logic_circuit() -> BinaryQuadraticModel:
    """ d = A + BC'D + CD' + B'C + B'D'."""
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
    gates = quicksum(
        [bqm_gate1, bqm_gate2, bqm_gate3, bqm_gate4, bqm_gate5, 
         bqm_gate6, bqm_gate7, bqm_gate8, bqm_gate9]
    )
    
    return gates


def e_logic_circuit() -> BinaryQuadraticModel:
    """ e = CD' + B'D'."""
    bqm_gate1 = and_gate('B', 'D', 'out21')
    bqm_gate1.flip_variable('B')
    bqm_gate1.flip_variable('D')
    bqm_gate2 = and_gate('C', 'D', 'out22')
    bqm_gate2.flip_variable('D')
    bqm_gate3 = or_gate('out21', 'out22', 'e')
    gates = quicksum([bqm_gate1, bqm_gate2, bqm_gate3])

    return gates


def f_logic_circuit() -> BinaryQuadraticModel:
    """ f = A + C'D' + BC' + BD'."""
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
    gates = quicksum(
        [bqm_gate1, bqm_gate2, bqm_gate3, 
         bqm_gate4, bqm_gate5, bqm_gate6]
    )
    
    return gates


def g_logic_circuit() -> BinaryQuadraticModel:
    """ g = A + BC' + CD' + B'C."""
    bqm_gate1 = and_gate('B', 'C', 'out30')
    bqm_gate1.flip_variable('C')
    bqm_gate2 = and_gate('C', 'D', 'out31')
    bqm_gate2.flip_variable('D')
    bqm_gate3 = and_gate('B', 'C', 'out32')
    bqm_gate3.flip_variable('B')
    bqm_gate4 = or_gate('out30', 'out31', 'out33')
    bqm_gate5 = or_gate('A', 'out32', 'out34')
    bqm_gate6 = or_gate('out33', 'out34', 'g')
    gates = quicksum(
        [bqm_gate1, bqm_gate2, bqm_gate3, 
         bqm_gate4, bqm_gate5, bqm_gate6]
        )
    
    return gates


def seven_segment_display_circuit(input_signal: str) -> BinaryQuadraticModel:
    """ Creates the BQM of the circuit.
    
        It calls the functions that forms the bqm for the different outputs,
        it creates a big BQM that correspond to all output signals and set
        the input variables into a specific value in order to create only
        one possible state with the lowest energy.

        Args:
            input_signal: A string of a number in binary form for the input
            of the circuit.

        Returns:
            A dimod.BinaryQuadraticModel corresponds to the BCD to 7
            segment display decoder for a specific input.  
    """
    # collects all bqms for each output signal.
    bqm = quicksum(
        [a_logic_circuit(), b_logic_circuit(), c_logic_circuit(), d_logic_circuit(),
         e_logic_circuit(), f_logic_circuit(), g_logic_circuit()]
    )
    # creates a list with the values of the input in 4 binary values.
    signal = [int(digit) for i, digit in enumerate(input_signal) if i > 1]
    # defines the values of the variables input.
    bqm.fix_variables(
        [('A', signal[0]), ('B', signal[1]), ('C', signal[2]), ('D', signal[3])]
    )

    return bqm


def solve_bqm(
        bqm: BinaryQuadraticModel, 
        reads: int = 1000, 
        desc: str = '7 segment display circuit'
        ) -> SampleSet:
    """ Solves a BQM using DWaveSampler and EmbeddingComposite.
    
        The simplest way to use quantum material for solving a bqm is 
        to call the DWaveSampler with the EmbeddingComposite in order to
        automate minor embedding (mapping the variables into qubits).

        Args:
            bqm: The Binary Quadratic Problem that we use the solver 
            reads: number of times that the solver samples from bqm.
            desc: The description of the problem.

        Returns:
            A dimod.SampleSet with the output signals of the circuit.
    """
    sampler = EmbeddingComposite(DWaveSampler())
    samples = sampler.sample(bqm, num_reads=reads, label=desc)
    # Keeps only the variables of the circuit's output for display,
    # the interior variables are not visible somewhere.
    samples = keep_variables(samples, ['a', 'b', 'c', 'd', 'e', 'f', 'g'])
    
    return samples


def format_output(
        samples: SampleSet, 
        rows: int = 11, 
        columns: int = 5
        ) -> ndarray:
    """ Represents sampler's answer into an array.
    
        It takes the lowest energy sample and change the value of the 
        array that is initially full with zeros in order to look like 
        a led display.

        Args:
            samples: The samples of the bqm.
            rows: The dows of the array.
            columns: The columns of the array.
        
        Returns:
            A numpy.array that correspond to the output. 
    """
    display = zeros((rows,columns))
    for key, val in samples.first[0].items():
        if val == 0:
            continue
        elif key == 'a':
            display[0 , 1:columns-1] = 1
        elif key == 'b':
            display[1:rows//2 , columns-1] = 1
        elif key == 'c':
            display[rows//2+1:rows-1 , columns-1] = 1
        elif key == 'd':
            display[rows//2 , 1:columns-1] = 1
        elif key == 'e':
            display[rows//2+1:rows-1 , 0] = 1
        elif key == 'f':
            display[1:rows//2 , 0] = 1
        elif key == 'g':
            display[rows-1 , 1:columns-1] = 1

    return display


def create_output_file(answer: SampleSet, display: ndarray) -> None:
    """ Writes the results of the code into a file."""
    with open('output.txt', 'w') as f:
        f.write('The display is:\n\n')
        rows = []
        for row in display:
            single_row = [str(i) if i == 1 else '   ' for i in row]
            rows.append(' '.join(single_row))
        display_string = '\n'.join(rows)
        f.write(display_string)
        f.write('\n\nThe Results from the sampler are below.\n\n')
        f.write(str(answer))


def main():
    user_input = format_input()
    bqm = seven_segment_display_circuit(user_input)
    answer = solve_bqm(bqm, desc=f'Circuit ABCD:{user_input[2:]}')
    display = format_output(answer)
    create_output_file(answer, display)


if __name__ == '__main__':
    main()
