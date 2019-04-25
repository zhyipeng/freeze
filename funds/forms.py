from rest_framework import serializers

from funds.models import Fund, FundLog, InvestmentLog


class AddFundDataForm(serializers.Serializer):
    fund_id = serializers.PrimaryKeyRelatedField(queryset=Fund.objects.all())
    value = serializers.FloatField()
    date = serializers.DateField()

    def create(self, validated_data):
        fund = validated_data.pop('fund_id')
        instance, _ = FundLog.objects.update_or_create(
            fund=fund,
            date=validated_data['date'],
            defaults={'value': validated_data['value']})

        return instance


class AddInvestLogForm(AddFundDataForm):
    OPTION_BUY = 'buy'
    OPTION_SELL = 'sell'

    option = serializers.ChoiceField(choices=(OPTION_BUY, OPTION_SELL))

    def create(self, validated_data):
        option = validated_data.pop('option')
        if option == self.OPTION_SELL:
            validated_data['value'] = -validated_data['value']

        fund = validated_data.pop('fund_id')
        instance = InvestmentLog.objects.create(
            fund=fund,
            user=self.context['user'],
            **validated_data
        )

        return instance
