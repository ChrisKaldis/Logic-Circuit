import dwavebinarycsp.factories.constraint.gates as gates
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

        binary_user_input = bin(user_input)[2:]
        length_ = len(binary_user_input)
        digits = [i for i in binary_user_input]

        # In case number is not 8 or 9 it is represented in binary with
        # less than 4 digits so we add zeros in order to have a proper 
        # input in our gates that correspond to contraints.
        for _ in range(length_, 4):
            digits.insert(0, '0')
        binary_user_input = ''.join(digits)

        return binary_user_input

def seven_segment_display_circuit():
    """Solve the constraint satisfaction problem of the circuit."""
    pass

def format_output():
    """Represents basic information of the sampler's answer."""
    pass

def main():
    pass

if __name__ == '__main__':
    main()
