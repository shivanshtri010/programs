#!/usr/bin/env python3

import sys
import unittest


def prime(n):
    
             
             if n>1:
                 for i in range(2,n//2+1):
                        if(n%i==0):
                             return "{} is not a prime number".format(n)
                              
                 else:
                    return "{} is a prime number".format(n)

             elif n==1:
                 return "1 is not a prime number"
             else:
                 return "Enter a positive number"
                 
def check_p(a):
    if a== None:
        print("Test Passed")
    else :
        print("Test Failed")

class TestPrime(unittest.TestCase):
    def test1_basic(self):
        testcase = 79217
        expected ="79217 is not a prime number" 
        check_p(self.assertEqual(str(prime(testcase)),expected))

    def test2_basic(self):
        testcase = -190
        expected ="Enter a positive number"
        check_p(self.assertEqual(str(prime(testcase)),expected))
        
    def test2_basic(self):
        testcase = 10
        expected ="10 is not a prime number"
        check_p(self.assertEqual(str(prime(testcase)),expected))

    def test3_basic(self):
        testcase =1 
        expected ="1 is not a prime number"
        check_p(self.assertEqual(str(prime(testcase)),expected))

    def test4_basic(self):
        testcase = 99991
        expected ="99991 is a prime number"
        check_p(self.assertEqual(str(prime(testcase)),expected))


unittest.main()

