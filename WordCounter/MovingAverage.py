__author__ = 'tina'

from collections import deque

"""
Moving averages: given a sequence of values, the simple moving average of the last n values is the sum of the last n
values divided by n. When a new value is added, the oldest drops off the end in computing the new average.
a) Write a Python function moving_average() that takes an integer parameter n and returns a closure that takes a single
argument x and returns the "moving average" of the last n values of x (if the closure has been called less than n times,
return None).

b) Write a Python class MovingAverage that creates a callable object that does the same thing.

For efficiency, use a circular buffer or collections.deque to store the data points. Why is using a straight list a
performance problem?
"""


def moving_average(numItems):
    ma_deque = deque()

    def computeMovingAverage(y):
        ma_deque.append(y)
        if len(ma_deque) > numItems:
            ma_deque.popleft()
        total = 0
        for number in ma_deque:
            total += number
        return (total * 1.0) / len(ma_deque)

    return computeMovingAverage


class MovingAverage:
    def __init__(self, maxItems):
        self.ma_deque = deque()
        self.maxItems = maxItems

    def __call__(self, number):
        self.ma_deque.append(number)
        if len(self.ma_deque) > self.maxItems:
            self.ma_deque.popleft()
        total = 0
        for number in self.ma_deque:
            total += number
        return (total * 1.0) / len(self.ma_deque)


ma_closure = moving_average(5)
print ma_closure(1)
print ma_closure(5)
print ma_closure(7)
print ma_closure(19)
print ma_closure(32)
print ma_closure(11)



ma_callable = MovingAverage(5)
print ma_callable(1)
print ma_callable(5)
print ma_callable(7)
print ma_callable(19)
print ma_callable(32)
print ma_callable(11)
