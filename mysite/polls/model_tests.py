from django.test import TestCase

# Create your tests here.
import datetime

from django.utils import timezone
from django.test import TestCase

from polls.models import Question

class QuestionModelTests(TestCase):

 

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


if __name__=='__main__':
    ## run with python manage.py  test  polls.tests.model_tests
    ## or with  python manage.py  test  polls.tests.model_tests.QuestionModelTests
    ## or with  python manage.py  test  polls.tests.model_tests.QuestionModelTests.test_was_published_recently_with_future_question
    ## or in shell with
    from polls.tests.model_tests import QuestionModelTests
    import unittest
    suite = unittest.TestLoader().loadTestsFromTestCase( QuestionModelTests)
    ttrunner1  = unittest.TextTestRunner(verbosity=2)
    ttresult1  = ttrunner1.run(suite)
    ttresult1.testsRun
    ttresult1.errors
    ttresult1.failures
