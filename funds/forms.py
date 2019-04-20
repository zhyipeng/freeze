from rest_framework import serializers

from core import exceptions
from funds.models import Fund


class AddConcernedFundForm(serializers.Serializer):
    fund_id = serializers.IntegerField()

    def validate_fund_id(self, value):
        if not Fund.objects.filter(id=value).exists():
            raise serializers.ValidationError('该基金不存在')

        user = self.context['user']
        if value in user.concerned_funds:
            raise exceptions.BusinessException(exceptions.FUND_HAD_CONCERNED)

        return value

    def create(self, validated_data):
        user = self.context['user']
        user.concerned_funds.append(validated_data['fund_id'])
        user.save(update_fields=['concerned_funds'])

        return user


class RemoveConcernedFundForm(serializers.Serializer):
    fund_id = serializers.IntegerField()

    def validate_fund_id(self, value):
        if not Fund.objects.filter(id=value).exists():
            raise serializers.ValidationError('该基金不存在')

        user = self.context['user']
        if value not in user.concerned_funds:
            raise serializers.ValidationError('该基金已从关注列表移除')

        return value

    def create(self, validated_data):
        user = self.context['user']
        user.concerned_funds.remove(validated_data['fund_id'])
        user.save(update_fields=['concerned_funds'])

        return user
