import os
from locust import HttpUser, task, constant


recommendations_client_host = os.getenv("RECOMMENDATIONS_CLIENT_HOST", "localhost")

max_results = 100_000


class MarketPlaceTestUser(HttpUser):
    host = f"http://{recommendations_client_host}:3333"
    wait_time = constant(0)

    def on_start(self):
        return super().on_start()

    def on_stop(self):
        return super().on_stop()

    @task
    def get_recommend_books_grpc(self):
        self.client.get(f"{self.host}/grpc/{max_results}")

    @task
    def get_recommend_books_rest(self):
        self.client.get(f"{self.host}/rest/{max_results}")
