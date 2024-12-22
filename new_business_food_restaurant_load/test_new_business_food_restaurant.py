from locust import TaskSet, task, HttpLocust
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from new_business_food_restaurant_load import load_test_helper


class NewBusinessFoodRestaurant(TaskSet):

    @task(1)
    def StartNocProcess(self):
        load_test_helper.post(self.client, "StartNocProcess", "ADFCA", "StartNocProcess")


class AllTests(HttpLocust):
    host = load_test_helper.host
    task_set = NewBusinessFoodRestaurant
    min_wait = 5000
    max_wait = 15000
