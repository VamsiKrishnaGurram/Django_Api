from rest_framework import serializers
from .models import *

class roleSerializer(serializers.ModelSerializer):
	class Meta:
		model = roles
		fields = ('__all__')


class pollingSerializer(serializers.ModelSerializer):
	class Meta:
		model = polling
		fields = ('__all__')		