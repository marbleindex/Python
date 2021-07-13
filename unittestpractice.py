## HOMEWORK 7: UNITTEST

# Purpose: use unittest.TestCase methods to confirm correct addition and subtraction of date and timedelta objects

import datetime
import unittest

## create some datetime objects to add and subtract
f20start = datetime.datetime(2020,8,17,9,0,0,0)
f20end = datetime.datetime(2020,12,18,18,0,0,0)
s21start = datetime.datetime(2021,1,19,8,30,0,0)
reviewsDue = datetime.datetime(2020,10,18,0,0,0,0)

# create a class with functions to add and subtract dates
class createTimedeltas():
        def academic_calendar_length(semester_start,semester_end):
                length = semester_end - semester_start
                return length
        def additive_academic_calendar_length(semester_start, semester_end):
                return semester_start + createTimedeltas.academic_calendar_length(semester_start,semester_end)

# create a testing class with timedeltas
# include functions that test both the addition and subtraction functions in the createTimedeltas class
# try a few different assert statements
class testDate(unittest.TestCase):
        def testSemsterLength(self):
                fallSemesterLength = datetime.timedelta(days = 123, hours = 9)
                self.assertEqual(createTimedeltas.academic_calendar_length(f20start,f20end),fallSemesterLength)

        def testBreakLength(self):
                winterBreakLength = datetime.timedelta(days = 31, hours = 14, minutes = 30)
                self.assertEqual(createTimedeltas.academic_calendar_length(f20end,s21start),winterBreakLength)

        def testBreakStarts(self):
                self.assertEqual(createTimedeltas.additive_academic_calendar_length(s21start,f20end),f20end)

        def testStillF2020(self):
                self.assertLessEqual(datetime.datetime.today(),f20end)

        def testReviewsOnTime(self):
                self.assertTrue(datetime.datetime(2020,10,11,0,0,0,0) <= datetime.datetime.today() <= reviewsDue)

# run the unittest main function
if __name__ == '__main__':
        unittest.main()
