"""
Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n.

A 1-interesting polygon is just a square with a side of length 1. 

An n-interesting polygon is obtained by taking the n - 1-interesting polygon and appending 1-interesting polygons to its rim, side by side. 

You can see the 1-, 2-, 3- and 4-interesting polygons in the picture below.
"""

def solution(n):
    """
        As there are already coding examples, I will explain why the formula is n * n + (n-1) * (n-1)

    You need to see the graph diagonally
    You will notice that the sides are always n
    For example, if n=4, the shape has for 4 squares on each side, thus n * n
    However, if you notice, n * n does not account for all the squares. There are    squares in between the once you accounted for
   
    Take away the square you have accounted with n * n, you will notice now that the side of the shape is now n-1
   
    Thus, you take into account of the squares in between, the formula is n * n + (n-1) * (n-1)
    
    Example: if n = 4, the outer square is 4 * 4 = 16. Then take away the area you have just calculated, the inner squares is 3 * 3 = 9. Add together, you get 25.
    """
    # return 2 * n * (n-1) + 1
    # return (n**2)+((n-1)**2)
    return n * n + (n-1) * (n-1)

