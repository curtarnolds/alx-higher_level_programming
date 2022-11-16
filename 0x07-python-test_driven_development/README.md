# Test Driven Development

In this project I have learnt the following:
* An interactive test: This is the kind of test in which the python interactive shell is replicated in the docstring of code. This allows the `doctest` module to run the shell replicas and compare them with the outputs that are provided
* Tests allow engineers the opportunity to check if the code they write or programs they build would run efficiently.
* You write Docstrings to create tests by simply running code in the python interactive shell and then copying and pasting it in your docstring. Note that docstrings begin and end with tripple quotes
* Module documentation comes as the first text before any function or class is written. The class/function documentation is written immediately after the function is declared, before any code is written
* Some of the basic option flags used when writing tests include;
  * doctest.ELLIPSIS
  * doctest.NORMALIZE_WHITESPACE
* Edge cases are found by testing the function at boundary beyond which the funtion is  not valid