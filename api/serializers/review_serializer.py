from django.shortcuts import get_object_or_404
from rest_framework import serializers

from ..models import Review, Title


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)

    def validate(self, data):
        if self.context['request'].method != 'POST':
            return data
        title = get_object_or_404(
            Title,
            pk=self.context['view'].kwargs.get('title_id')
        )
        author = self.context['request'].user
        queryset = Review.objects.filter(author=author, title=title)
        if queryset.exists():
            raise serializers.ValidationError(
                'Вы можете оставить только одно ревью.'
            )
        return data

    class Meta:
        fields = ['id', 'text', 'author', 'score', 'pub_date']
        model = Review
