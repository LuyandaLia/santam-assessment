
def validate_claim(func):
    def wrapper(*args, **kwargs):
        if args[1] <= args[2].cover:
            return func(*args, **kwargs)
        else:
            raise ValueError("Claim amount exceeds coverage")

    return wrapper


class Policy:
    def __init__(self, policy_number: str, holder_name: str, holder_age: int):
        self.premium = None
        self.policy_number = policy_number
        self.holder_name = holder_name
        self.holder_age = holder_age
        self.claims = []
        self.assets = []
        self.asset_types = {
            "Bicycles": 0.03,
            "Home Appliances": 0.02,
            "Tech": 0.05,
            "Default": 0.01,
        }

    @validate_claim
    def make_claim(self, claim_amount: float, asset: object):
        self.claims.append(claim_amount)

    def calculate_premium(self, assets: list) -> float:
        total_premium = 0.0
        for asset in assets:
            total_premium += asset.cover * self.asset_types.get(
                asset, self.asset_types["Default"]
            )
        self.premium = total_premium
        return self.premium


class Asset:
    def __init__(self, name: str, value: float, cover: float, asset_type: str, serial_number=None):
        self.name = name
        self.value = value
        self.cover = cover
        self.asset_type = asset_type
        self.serial_number = serial_number

    def __call__(self, policy):
        policy.assets.append(self)



policy_holder: str = "Alice"
policy = Policy("P12345", policy_holder, 35)

bicycle = Asset("Mountain Bike", 35000, 40000, "Bicycles")
bicycle(policy)

refrigerator = Asset("Refrigerator", 5500, 7000, "Home Appliances", policy)
refrigerator(policy)

laptop = Asset("Laptop", 16000, 18000, "Tech", policy)
laptop(policy)


policy.make_claim(500, refrigerator)
policy.make_claim(11000, laptop)

print("Policy Number: " + policy.policy_number)
print("Premium: " + str(policy.calculate_premium(policy.assets)))
print("Claims: " + str(policy.claims))

print("Assets:")
for asset in policy.assets:
    print("\t" + asset.name + ": " + str(asset.value))
