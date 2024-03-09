# Logic-Circuit

Logic circuit problem on a D-Wave quantum computer. This 
repository is a first attempt to understand basic 
features of ocean software. Strongly recommend to read
the [Getting Started][def0] tutorial first. The circuit 
represents a 7-segment display that is commonly used in
household appliances and it is usually analyzed in 
logic circuit design books.

## Set up the Enviroment

For the project development it was used a virtual enviroment.
Below you can see the commands that i used in my linux based
computer to create it.

```
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

After that, you follow the [steps][def1] in order to configure
access to Leap's Solvers.

[def0]: https://docs.ocean.dwavesys.com/en/stable/overview/install.html
[def1]: https://docs.dwavesys.com/docs/latest/doc_leap_dev_env.html#authorizing-access-to-leap