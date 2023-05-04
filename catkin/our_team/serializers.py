from rest_framework import serializers
from .models import TeamMember, Designation


class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = '__all__'


class TeamMemberSerializer(serializers.ModelSerializer):

    designation_info = DesignationSerializer(read_only=True, source='designation')
    designation = serializers.IntegerField(write_only=True)

    class Meta:
        model = TeamMember
        fields = ['id', 'name', 'employee_id', 'designation_info', 'designation', 'linked_in_link', 'profile_link', 'image_url']
    

    def create(self, validated_data):
        designation_id = validated_data.pop('designation')

        member = TeamMember.objects.create(designation_id=designation_id, **validated_data)
        member.save()
        
        return member
    
    def update(self, instance, validated_data):
        designation_id = validated_data.pop('designation')
        instance.designation_id = designation_id
        return super().update(instance, validated_data)