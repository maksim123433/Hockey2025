from rest_framework import serializers
from clubs.models import Clubs
from matches.models import Matches
from authorization.models import ProUser

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clubs
        fields = '__all__'

    def create(self, validated_data):
        return Clubs.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.Name = validated_data.get('Name', instance.Name)
        instance.Foundation_date = validated_data.get('Foundation_date', instance.Foundation_date)
        instance.Head_coach = validated_data.get('Head_coach', instance.Head_coach)
        instance.Number_of_players = validated_data.get('Number_of_players', instance.Number_of_players)
        instance.Owner = validated_data.get('Owner', instance.Owner)
        instance.Conference = validated_data.get('Conference', instance.Conference)
        instance.Total_cost_of_club = validated_data.get('Total_cost_of_club', instance.Total_cost_of_club)
        instance.save()
        return instance



class ProuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProUser
        fields = '__all__'

    def create(self, validated_data):
        return ProUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.role = validated_data.get('role', instance.role)
        instance.save()
        return instance



class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matches
        fields = '__all__'

    def create(self, validated_data):
        return Matches.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.home_team = validated_data.get('home_team', instance.home_team)
        instance.away_team = validated_data.get('away_team', instance.away_team)
        instance.match_date = validated_data.get('match_date', instance.match_date)
        instance.venue = validated_data.get('venue', instance.venue)
        instance.save()
        return instance


