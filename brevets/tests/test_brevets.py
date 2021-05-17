"""
Nose tests for acp_times.py
"""
from acp_times import open_time, close_time
from nose.tools import *
import arrow
import nose    # Testing framework
import logging

logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)


def test_open_times():
    """
    A series of testing that testing open_times in 0, 60, 200, 300, 400, 600, 1000km
    """
    testting_time = arrow.now.format()
    assert str(open_time(0, 200, testing_time)) == str(testing_time)                        # Testing for 0km
    assert str(open_time(60, 200, testing_time)) == str(testing_time.shift(minutes=106))    # Testing for 60km
    assert str(open_time(200, 200, testing_time)) == str(testing_time.shift(minutes=353))   # Testing for 200km
    assert str(open_time(300, 200, testing_time)) == str(testing_time.shift(minutes=541))   # Testing for 400km
    assert str(open_time(400, 400, testing_time)) == str(testing_time.shift(minutes=728))   # Testing for 400km
    assert str(open_time(600, 600, testing_time)) == str(testing_time.shift(minutes=1128))   # Testing for 600km
    assert str(open_time(1000,1000, testing_time)) == str(testing_time.shift(minutes=1985))   # Testing for 1000km

def test_close_time():
    """
    A series of testing that testing close_times in 0, 60, 200, 300, 400, 600, 1000km
    """
    testting_time = arrow.now.format()
    assert str(close_time(0, 200, testing_time)) == str(testing_time.shift(minutes=60))      # Testing for 0km
    assert str(close_time(60, 200, testing_time)) == str(testing_time.shift(minutes=240))    # Testing for 60km
    assert str(close_time(200, 200, testing_time)) == str(testing_time.shift(minutes=800))   # Testing for 200km
    assert str(close_time(300, 200, testing_time)) == str(testing_time.shift(minutes=1200))   # Testing for 400km
    assert str(close_time(400, 400, testing_time)) == str(testing_time.shift(minutes=1600))   # Testing for 400km
    assert str(close_time(600, 600, testing_time)) == str(testing_time.shift(minutes=2400))   # Testing for 600km
    assert str(close_time(1000,1000, testing_time)) == str(testing_time.shift(minutes=4500))   # Testing for 1000km

def test_invalid_user_input():
    """
    Testing different of invalid inputs
    """
    testting_time = arrow.now.format()
    assert open_time(-60, 200, testing_time)                    #Testing with a negative number
    assert close_time(-60, 200, testing_time)
    assert open_time(60.123456, 200, testing_time)              #Testing with a float number
    assert close_time(60.123456, 200, testing_time)
    assert open_time("20", 200, testing_time)                   #Testing with a string 20
    assert close_time("20", 200, testing_time)
    assert open_time(, 200, testing_time)                       #Testing with an empty value
    assert close_time(, 200, testing_time)
    
