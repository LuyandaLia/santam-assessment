from django.db import models
from django_model_example import PolicyHolder

policyholders = PolicyHolder.objects.annotate(sset_count=models.Count('policy__asset')).filter(asset_count__gt=1)

