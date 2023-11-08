from dataclasses import dataclass
from typing import Optional


@dataclass
class Policy:
    """
    Discuss the concept of data classes in Python and explain how they can be beneficial in
    your insurance system. Provide an example of a data class and demonstrate its usage.
    """
    policy_number: str
    policy_holder: str
    holder_age: int
    claims: Optional[list] = list
    assets: Optional[list] = list


policy = Policy("P12345", "Alice", 35)
print("Policy Number: " + policy.policy_number)
