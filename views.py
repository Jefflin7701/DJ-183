import sys
sys.path.append("controllers")

"""
To allow our website to see our different controllers, we must import them using
this views.py file. The syntax is as follows:

from A import B

where A is a Python file in the /controllers folder (without the .py!) and B is
the name of the function that runs that particular route.

For every route, you must import it in this file. An example for the starter
code is given below. Continue adding more as you make more routes.
"""

from index import *
from question import *
from answer import *
from clear import *
from confirm import *
from username import *
from leaderboard import *
from enteruser import *
from about import *
from creators import *
from game import *
