import dwavebinarycsp.factories.constraint.gates as gates
from dwave.system import DWaveSampler, EmbeddingComposite


def format_input():
    """Creates the binary representation of a single digit decimal number."""

    range_ = range(0,10)
    user_input = input("Select a single digit number:")

    try:
        user_input = int(user_input)
    except ValueError:
        print("Input type must be int")

    if user_input not in range_:
        print("Input must be between [0,9]")

    binary_user_input = bin(user_input)[2:]
    length_ = len(binary_user_input)

    if length_ < 4:
        binary_user_input = '0' * (4 - length_) + binary_user_input

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
