# Logic-Circuit

Logic circuit problem on a D-Wave quantum computer. This 
repository is a first attempt to understand basic 
features of ocean software. Strongly recommend to read
the [Getting Started][def0] tutorial first. The circuit 
represents a 7-segment display that is commonly used in
household appliances and it is usually analyzed in 
logic circuit design books. This repository is based on
the [factoring][def1] example that has similar logic.

## Set up the Enviroment for Developing

For the project development it was used a virtual enviroment.
Below you can see the commands that i used in my linux based
computer to create it.

```
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

After that, you follow these [steps][def2] in order to configure
access to Leap's Solvers.

## Code Overview

The logic circuit that is designed and solved is a 
[BCD to 7 segment display decoder][def3]. You can find the 
truth table and the karnaugh's maps in many website on
the internet. A basic description of the circuit is that you have 
4 binary digits as an input that can be a number from 0 to 9 
(single digit decimal number) and the output is a combination of
7 signals that correspond in a different led display digit.

Like the factoring example we transform the circuit into a
binary quadratic problem that as we know D-Wave's 
quantum computer is capable of solving.

### Structure of code

The different parts of the code can be summarized into the functions
that main() calls and are shown below:

```python
def main():
    user_input = format_input()
    bqm = seven_segment_display_circuit(user_input)
    answer = solve_bqm(bqm, desc=f'Circuit ABCD:{user_input[2:]}')
    display = format_output(answer)
    create_output_file(answer, display)
```

So in format_input() the user input is formulated properly for the 
creation of the Binary Quadratic Model that is being made in 
seven_segment_display_circuit(). After that a solver which is a 
quantum sampler is called and we get an answer that are the 
samples of the BQM, format_output() creates an array for a 
minimal graphic display representation and create_output_file()
gather other the information of the code in a file.

[def0]: https://docs.ocean.dwavesys.com/en/stable/overview/install.html
[def1]: https://github.com/dwave-examples/factoring
[def2]: https://docs.dwavesys.com/docs/latest/doc_leap_dev_env.html#authorizing-access-to-leap
[def3]: https://www.electronicshub.org/bcd-7-segment-led-display-decoder-circuit/