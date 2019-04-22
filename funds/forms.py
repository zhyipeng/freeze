from rest_framework import serializers

from funds.models import Fund, FundLog


class AddFundDataForm(serializers.Serializer):
    fund_id = serializers.PrimaryKeyRelatedField(queryset=Fund.objects.all())
    value = serializers.FloatField()
    date = serializers.DateField()

    def create(self, validated_data):
        fund = validated_data.pop('fund_id')
        instance, _ = FundLog.objects.update_or_create(
            fund=fund, defaults=validated_data)

        return instance
