import time

from django.db import models

class MyModel(models.Model):
    def process(self):
        print("Sleeping for 15 seconds...")
        time.sleep(15)
        print("Wait is over!")
