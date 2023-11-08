from django.db import models


class Policy(models.Model):
    policy_number = models.CharField(max_length=20, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    coverage_type = models.CharField(max_length=50)
    premium_amount = models.DecimalField(max_digits=10, decimal_places=2)
    assets = models.TextField(null=True)
    claims = models.TextField(null=True)

    policy_holder = models.ForeignKey('PolicyHolder', on_delete=models.CASCADE)

    def __str__(self):
        return self.policy_number


class PolicyHolder(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    age = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Asset(models.Model):
    name = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    cover = models.DecimalField(max_digits=10, decimal_places=2)
    asset_type = models.CharField(max_length=15)
    serial_number = models.CharField(max_length=15, null=True, blank=True)

    policy = models.ForeignKey('Policy', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.asset_type} - {self.value}"
