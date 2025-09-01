from faker.generator import random
from faker.proxy import Faker

class ReinstatementResponsibleMother:
    def __init__(self):
        self.faker = Faker()

    def get(self):
        first_name = self.faker.first_name()
        last_name = self.faker.last_name()
        email = f"{first_name.lower()}.{last_name.lower()}@example.com"
        return {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "uuid": self.faker.uuid4(),
            "status": random.choice(["Active", "Inactive"]),
        }

    def get_multiple(self, count: int):
        return [self.get() for _ in range(count)]