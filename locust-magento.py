from locust import HttpLocust, TaskSet, task


class WebsiteTasks(TaskSet):
    @task
    def product1(self):
        self.client.get("/madison-island-vip-membership-1-year.html")

    @task
    def product2(self):
        self.client.get("/aviator-sunglasses.html")

    @task
    def product3(self):
        self.client.get("/jackie-o-round-sunglasses.html")

    @task
    def product4(self):
        self.client.get("/retro-chic-eyeglasses.html")

    @task
    def product5(self):
        self.client.get("/linen-blazer-585.html")

    @task
    def product6(self):
        self.client.get("/chelsea-tee-720.html")

    @task
    def product7(self):
        self.client.get("/tori-tank-590.html")

    @task
    def product8(self):
        self.client.get("/elizabeth-knit-top-596.html")

    @task
    def product9(self):
        self.client.get("/racer-back-maxi-dress-608.html")

    @task
    def product10(self):
        self.client.get("/lafayette-convertible-dress.html")

    @task
    def product11(self):
        self.client.get("/a-tale-of-two-cities.html")

    @task
    def product12(self):
        self.client.get("/alice-in-wonderland.html")

    @task
    def product13(self):
        self.client.get("/khaki-bowery-chino-pants.html")

    @task
    def product14(self):
        self.client.get("/around-the-world-in-80-days.html")

    @task
    def product15(self):
        self.client.get("/falling-by-i-am-not-lefthanded.html")

    @task
    def product16(self):
        self.client.get("/if-you-were-by-keshco.html")

    @task
    def product17(self):
        self.client.get("/can-t-stop-it-by-shearer.html")

    @task
    def product18(self):
        self.client.get("/love-is-an-eternal-lie-by-the-sleeping-tree.html")

    @task
    def product19(self):
        self.client.get("/fire-kalima-remix-by-unannounced-guest.html")

    @task
    def product20(self):
        self.client.get("/broadway-pump.html")

    @task
    def product21(self):
        self.client.get("/park-avenue-pleat-front-trousers-673.html")

    @task
    def product22(self):
        self.client.get("/body-wash-with-lemon-flower-extract-and-aloe-vera.html")

    @task
    def product23(self):
        self.client.get("/bath-minerals-and-salt.html")

    @task
    def product24(self):
        self.client.get("/shea-enfused-hydrating-body-lotion.html")

    @task
    def product25(self):
        self.client.get("/titian-raw-silk-pillow.html")

    @task
    def product26(self):
        self.client.get("/shay-printed-pillow.html")

    @task
    def product27(self):
        self.client.get("/carnegie-alpaca-throw.html")

    @task
    def product28(self):
        self.client.get("/park-row-throw.html")

    @task
    def product29(self):
        self.client.get("/gramercy-throw.html")

    @task
    def index(self):
        self.client.get("/")

    @task
    def sitemap(self):
        self.client.get("/catalog/seo_sitemap/category/")

    @task
    def homedecor(self):
        self.client.get("/home-decor.html")


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 5000
    max_wait = 15000
