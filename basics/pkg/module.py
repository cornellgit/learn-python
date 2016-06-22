from basics.pkg.fibo import fib_seq
# Python module can be as a singleton.

# 1. absolute path
# import fibo as fi
# from fibo import fib_seq as seq
# from fibo import *, not a good practice

# 2. relative path
# import from relative path
# from . import echo
# from .. import formats

print(fib_seq(5))

# 3. print locations python look for modules
# import sys
#
# for loc in sys.path:
#     print(loc)
