from django.test import TestCase

import threading

from MyApp.models import MyModel


class test_smtg(TestCase):
    def setUp(self):
        self.my_model = MyModel()
        self.my_model.save()

    def test_single_processing(self):
        self.my_model.process()

    def test_concurrent_processing(self):
        thread = threading.Thread(target=self.my_model.process)
        thread.start()
