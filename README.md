# Logic-Circuit

Logic circuit problem on a D-Wave quantum computer. This 
repository is a first attempt to understand basic 
features of ocean software. Strongly recommend to read
the [Getting Started][def0] tutorial first. The circuit 
represents a 7-segment display that is commonly used in
household appliances and it is usually analyzed in 
logic circuit design books. This repository is based on
the [factoring][def1] example that has similar logic.

## Code Overview

The logic circuit is designed and solved by a 
[BCD to 7 segment display decoder][def3]. You can find the 
truth table and the karnaugh's maps in many website on
the internet. A basic description of the circuit is that you have 
4 binary digits as an input that can be a number from 0 to 9 
(single digit decimal number) and the output is a combination of
7 signals that correspond in a different led display digit.

Like the factoring example we transform the circuit into a
binary quadratic problem that as we know D-Wave's 
quantum computer is capable of solving.

The solution of this problem is based on the `dimod` library, especially 
its generators of logic gates that returns objects of `BinaryQuadraticModel`
and make it simple to transpose complicated logic circuits into an objective function.

### Binary Quadratic Models

The binary quadratic model (BQM) class encodes Ising and quadratic unconstrained binary optimization (QUBO) models used by samplers such as the D-Wave system.

The BQM equation,

$E(v) = \sum_{i=1} a_iv_i + \sum_{i<j} b_{i,j}v_iv_j + c, \quad v_i \in \{-1, +1\} \quad \text{or} \quad \{0, 1\}$

read more in the [concepts page][def4].

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

First the function `format_input()` gets from the user a single digit decimal
number and returns the binary  representation in four digits that is used
by the function `seven_segment_display_circuit(user_input)`, this function
returns a binary quadratic model that describes the circuit. After that the 
`solve_bqm(bqm, desc=f'Circuit ABCD:{user_input[2:]}')` calls a quantum solver
and returns the set of samples for the binary quadratic model. The other two functions are just for a better representation. 

## Set up the Enviroment for Developing

For the project development it was used a virtual enviroment.
Below you can see the commands that i used in my linux based
computer to create it.

```
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

There is also a file for the Visual Studio Code Dev Containers extension
in order to use a docker, in that case you just download the requirements
with the same command.

After that, you follow these [steps][def2] in order to configure
access to Leap's Solvers.

You can then run the code as any other python file 

```
$ python3 logic_circuit.py
```

And check the unittest that use ExactSolver in order to see that the
bqm low energy state are equal with the circuit's truth table.

```
$ python -m unittest -v
```

[def0]: https://docs.ocean.dwavesys.com/en/stable/overview/install.html
[def1]: https://github.com/dwave-examples/factoring
[def2]: https://docs.dwavesys.com/docs/latest/doc_leap_dev_env.html#authorizing-access-to-leap
[def3]: https://www.electronicshub.org/bcd-7-segment-led-display-decoder-circuit/
[def4]: https://docs.ocean.dwavesys.com/en/stable/concepts/bqm.html