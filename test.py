import unittest
import random
from policy import Policy, Asset

from faker import Faker

faker = Faker()


class TestClientMethods(unittest.TestCase):

    def setUp(self):
        ages: tuple = (18, 24, 33, 56, 70)
        prefix: str = "P"
        self.cover: float = 40000
        value: float = 35000
        self.holder_age = random.choice(ages)
        self.policy_holder = faker.first_name()
        self.policy_number = f"{prefix}" + faker.ean()
        self.policy = Policy(self.policy_number, self.policy_holder, self.holder_age)
        self.bicycle = Asset("Mountain Bike", value, self.cover, "Bicycles")
        self.bicycle(self.policy)

    def tearDown(self):
        pass

    def test_make_claim_successful(self):
        claim_amount: float = 5000

        self.assertIsNone(self.policy.make_claim(claim_amount, self.bicycle))

    def test_make_claim_rejected(self):
        claim_amount: float = random.uniform(self.cover, float('inf'))
        with self.assertRaises(ValueError) as exc:
            self.policy.make_claim(claim_amount, self.bicycle)
        self.assertEqual(str(exc.exception), "Claim amount exceeds coverage")

    def test_policy_number_is_set(self):
        self.assertEqual(self.policy_number, self.policy.policy_number)

    def test_policy_has_asset(self):
        self.assertTrue(self.policy.assets)

    def test_policy_has_no_asset(self):
        self.policy.assets.clear()
        self.assertFalse(self.policy.assets)

    def test_calculate_premium(self):
        premium = 400.00
        self.assertEqual(self.policy.calculate_premium(self.policy.assets), premium)


if __name__ == '__main__':
    unittest.main()
