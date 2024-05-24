import uuid
from locust import HttpUser, task, between
from numpy import *
class MyUser(HttpUser):
    wait_time = between(1, 5)  # Espera entre 1 e 5 segundos entre cada tarefa
    host = "http://teste-MyLoad-jzrOySbExCWa-844009190.us-east-2.elb.amazonaws.com/"
    
    @task
    def my_task(self):
        body = {
            'UserID': f"{uuid.uuid4()}",
            'Title': f"{random.randint(0,100)}",
            'Text': 'Este é um texto de teste'
        }

        self.client.post("api/submit-form", json=body)
        
        response = self.client.get("api/submit-form")
        if response.status_code == 200:
            data = response.json()
            if data:
                print("GET request returned data:", data)
            else:
                print("GET request did not return any data")
        else:
            print("GET request failed with status code:", response.status_code)