from rest_framework import serializers

from .models import CandidateApplication

class CandidateApplicationSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="main:candidateapplication-detail")
    class Meta:
        model = CandidateApplication
        fields = ('url', 'first_name', 'last_name', 'date_of_birth', 'gender', 'contact_number', 'email')