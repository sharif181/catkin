from rest_framework import serializers
from .models import Feature, Category, Technology, Service


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    feature_info = FeatureSerializer(read_only=True, source='feature', many=True)
    feature = serializers.ListField(write_only=True)
    class Meta:
        model = Category
        fields = ['id', 'title', 'feature', 'feature_info']
    
    def create(self, validated_data):
        feature_ids = validated_data.pop('feature')

        category = Category.objects.create(**validated_data)
        category.save()
        for id in feature_ids:
            feature = Feature.objects.filter(pk=id).first()
            if feature:
                category.feature.add(feature)
        return category
    
    def update(self, instance, validated_data):
        feature_ids = validated_data.pop('feature')

        instance.feature.clear()
        for id in feature_ids:
            feature = Feature.objects.filter(pk=id).first()
            if feature:
                instance.feature.add(feature)
        return instance


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):

    feature_info = FeatureSerializer(read_only=True, source='features', many=True)
    features = serializers.ListField(write_only=True)

    category_info = FeatureSerializer(read_only=True, source='catagories', many=True)
    catagories = serializers.ListField(write_only=True)

    technology_info = FeatureSerializer(read_only=True, source='technologies', many=True)
    technologies = serializers.ListField(write_only=True)

    class Meta:
        model = Service
        fields = ['id', 'title', 'description', 'technologies', 
                  'technology_info', 'catagories', 'category_info', 
                  'features', 'feature_info']
        
    
    def create(self, validated_data):
        feature_ids = validated_data.pop('features')
        technologies_ids = validated_data.pop('technologies')
        catagories_ids = validated_data.pop('catagories')

        service = Service.objects.create(**validated_data)
        service.save()
        for id in feature_ids:
            feature = Feature.objects.filter(pk=id).first()
            if feature:
                service.features.add(feature)
        
        for id in technologies_ids:
            technology = Technology.objects.filter(pk=id).first()
            if technology:
                service.technologies.add(technology)

        for id in catagories_ids:
            category = Category.objects.filter(pk=id).first()
            if category:
                service.catagories.add(category)

        return service
    
    def update(self, instance, validated_data):
        feature_ids = validated_data.pop('features')
        technologies_ids = validated_data.pop('technologies')
        catagories_ids = validated_data.pop('catagories')

        instance.features.clear()
        instance.catagories.clear()
        instance.technologies.clear()
        

        for id in feature_ids:
            feature = Feature.objects.filter(pk=id).first()
            if feature:
                instance.features.add(feature)
        
        for id in technologies_ids:
            technology = Technology.objects.filter(pk=id).first()
            if technology:
                instance.technologies.add(technology)

        for id in catagories_ids:
            category = Category.objects.filter(pk=id).first()
            if category:
                instance.catagories.add(category)
                
        return super().update(instance, validated_data)