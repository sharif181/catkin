from rest_framework import serializers
from .models import ProjectImage, Project
from service.serializers import TechnologySerializer
from service.models import Technology


class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):

    image_info = ProjectImageSerializer(read_only=True, many=True, source='images')
    images = serializers.ListField(write_only=True)

    technology_info = TechnologySerializer(read_only=True, many=True, source='technologies')
    technologies = serializers.ListField(write_only=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'sub_title', 'description',
                   'live_preview_link', 'video_url', 
                   'technologies', 'technology_info', 
                   'images', 'image_info']
    

    def create(self, validated_data):
        images_id = validated_data.pop('images')
        technologies_ids = validated_data.pop('technologies')

        project = Project.objects.create(**validated_data)
        project.save()
        for id in images_id:
            project_image = ProjectImage.objects.filter(pk=id).first()
            if project_image:
                project.images.add(project_image)
        
        for id in technologies_ids:
            technology = Technology.objects.filter(pk=id).first()
            if technology:
                project.technologies.add(technology)

        return project
    
    def update(self, instance, validated_data):
        images_id = validated_data.pop('images')
        technologies_ids = validated_data.pop('technologies')

        instance.images.clear()
        instance.technologies.clear()
        

        for id in images_id:
            project_image = ProjectImage.objects.filter(pk=id).first()
            if project_image:
                instance.images.add(project_image)
        
        for id in technologies_ids:
            technology = Technology.objects.filter(pk=id).first()
            if technology:
                instance.technologies.add(technology)
        
        return super().update(instance, validated_data)