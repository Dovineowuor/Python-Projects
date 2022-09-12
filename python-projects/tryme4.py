def new_line():
    # This function is used for noting a new line. It creates a new line.

  print('')



def three_lines():
    # This function nests the new line function and hence the function 
    # new_line is reiterated to output 3 lines and hence meeting the need of three lines output.

  new_line()

  new_line()

  new_line()



def nine_lines():
    # This function nests three_lines function which also nests new_line 
    # function meeting the nine line task rule.

  three_lines()

  three_lines()

  three_lines()

#   When the function is called, it produces 9 lines due to the doubly nested new_line function 
# which is nested into the three line function.


def clear_screen():
    # This function clears the screen to meet the screen task instruction.
    # uses a combination of the functions nine_lines, three_lines, and new_line to print a total of twenty-five lines.

  nine_lines()

  three_lines()

  new_line()

#   "." is printed so as to shoe a border demarcation and the end of the function 
#    When the function is called it follows its predefined rules to realize a  semantic meaning

print('.')

new_line()

print('.')

three_lines()

print('.')

nine_lines()

print('.')

clear_screen()

# When the functions are called within the function, we realize that all the test cases are 
# met realizing 29 free lines printed and separated by a coma as from 
# the first to mark the first function, Second function three_lines at the 
# second  mark denoting the start of a new function the nine_lines and 
# finally clear_screen function which nests nine_lines function, 
# which nests the three_lines function which inturn nests new_line and hence a number
#  of 29 total new lines are realized from the code execution.

# Reference
# pythonanywhere. (2022). Host, run, and code Python in the cloud. Anaconda. https://www.pythonanywhere.com/