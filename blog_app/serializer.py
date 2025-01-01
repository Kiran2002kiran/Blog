from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Country , User , Blog


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'bio', 'date_of_birth']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user



class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id' , 'continent', 'country' , 'country_code'] 


class UserSerializer(serializers.ModelSerializer):
    country = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'date_of_birth', 'bio', 'country']

    def get_country(self,obj):
        request = self.context.get('request')
        if request and request.query_params.get('expand') == 'country':
            return CountrySerializer(obj.country).data if obj.country else None
        return obj.country_id


class BlogSerializer(serializers.ModelSerializer):
    # created_by = serializers.SerializerMethodField()
    created_by = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=True
    )

    
    class Meta:
        model = Blog
        fields = ['id' , 'title' , 'content' , 'created_at', 'created_by']


    def get_created_by(self , obj):
        request = self.context.get('request')
        if request and request.query_params.get('expand') == 'created_by':
            return UserSerializer(obj.created_by,context=self.context).data
        return obj.created_by.id

    

