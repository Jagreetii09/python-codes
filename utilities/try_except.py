# Errors detected during execution are called exceptions. It is possible
# to write programs that handle selected exceptions with a try-except statement.
# The try statement works as follows:
# 1. The statement(s) between the try and except keywords is executed.
# 2. If no exception happens, the except block  is skipped and execution
#    of the try statement is finished.
# 3. If an exception occurs during execution of the try clause, the rest
#    of the clause is skipped. Then if its type matches the exception
#    named after the except keyword, the except clause is executed, and
#    then execution continues after the try statement.
# 4. An unhandled exception stops the execution.
# 5. Optional else clause must follow all except clauses. It is useful
#    for code that must be executed if the try clause does not raise
#    an exception.

import sys
 
stop_codons = ['TAA', 'TAG', 'TGA']
print('Stop codons:', stop_codons)
 
while True:
    try:
         index = int(input('Please enter the index of a stop codon to print: '))
         print('Your codon is', stop_codons[index])
    except ValueError as ve:
         print(ve, 'Try again...')
    except IndexError:
         print('Your index', index, 'is out of range. Try again...')
    except:
         print('Unexpected error:', sys.exc_info()[0])
         sys.exit()
    else:
         print('Good bye!')
         break

