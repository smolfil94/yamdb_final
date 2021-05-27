from rest_framework import serializers

from ..models import Category, Genre, Title
from .category_serializer import CategorySerializer
from .genre_serializer import GenreSerializer


class TitleSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    genre = GenreSerializer(many=True)

    class Meta:
        fields = '__all__'
        model = Title


class GetTitleSerializer(TitleSerializer):
    genre = GenreSerializer(many=True)
    category = CategorySerializer()
    rating = serializers.IntegerField()


class PostTitleSerializer(TitleSerializer):
    category = serializers.SlugRelatedField(slug_field='slug',
                                            queryset=Category.objects.all(),
                                            required=False)
    genre = serializers.SlugRelatedField(slug_field='slug',
                                         queryset=Genre.objects.all(),
                                         many=True)
    year = serializers.IntegerField(required=False)
