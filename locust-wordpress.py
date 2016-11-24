from locust import HttpLocust, TaskSet, task


class WebsiteTasks(TaskSet):
    @task
    def index(self):
        self.client.get("/")

    @task
    def month(self):
        self.client.get("/2016/11/")

    @task
    def posts(self):
        for i in range(1, 200, 1):
            self.client.get('/{}/'.format(i), name='/[id]/')


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 5000
    max_wait = 15000
