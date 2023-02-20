"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    ### TODO
    pass

def longest_run(mylist, key):
    longest_run_length = 0
    current_run_length = 0
    for i in range(len(myarray)):
        if myarray[i] == key:
            current_run_length += 1
            if current_run_length > longest_run_length:
                longest_run_length = current_run_length
        else:
            current_run_length = 0
    return longest_run_length
    pass
# Work and span for longest_run is O(n). 

class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):
    n = len(mylist)
    if n == 0:
        return Result(0, 0, 0, False)
    elif n == 1:
        if mylist[0] == key:
            return Result(1, 1, 1, True)
        else:
            return Result(0, 0, 0, False)
    else:
        mid = n // 2
        left_result = longest_run_recursive(mylist[:mid], key)
        right_result = longest_run_recursive(mylist[mid:], key)
        left_size, right_size, longest_size = left_result.left_size, right_result.right_size, 0
        is_entire_range = False
        if left_result.is_entire_range and right_result.is_entire_range and mylist[mid-1] == key and mylist[mid] == key:
            is_entire_range = True
            longest_size = left_result.right_size + right_result.left_size
        elif left_result.is_entire_range:
            if mylist[mid-1] == key:
                left_size += right_result.left_size
            longest_size = max(left_result.longest_size, right_result.longest_size, left_size)
        elif right_result.is_entire_range:
            if mylist[mid] == key:
                right_size += left_result.right_size
            longest_size = max(left_result.longest_size, right_result.longest_size, right_size)
        else:
            longest_size = max(left_result.longest_size, right_result.longest_size, left_size, right_size)
        return Result(left_size, right_size, longest_size, is_entire_range)
    pass
#3d. The work is W(n) = 2W(n/2)+1 so O(n) and the span is also O(n) since its sequential. 
#3e. THe work is still O(n) and the span is O(log n) since its parallel. 

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3


