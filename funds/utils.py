from freeze import celery_app

from funds.models import FundLog, InvestmentLog
from utils.draw_tools import DrawTool

@celery_app.task()
def draw_fund(fund, user):
    value_list, date_list = [], []
    fund_logs = FundLog.objects.filter(
        fund=fund).order_by(
            'date').values_list('value', 'date')
    if fund_logs.exists():
        value_list, date_list = list(zip(*fund_logs))

    quantity_list, invest_date_list = [], []
    invest_logs = InvestmentLog.objects.filter(
        fund=fund, user=user).order_by('date').values_list('value', 'date')
    if invest_logs.exists():
        quantity_list, invest_date_list = list(zip(*invest_logs))

    tool = DrawTool()
    tool.draw_with_annotation(x=date_list,
                              y=value_list,
                              xx=invest_date_list,
                              anno=quantity_list)

    tool.save(f'{fund.code}.png')
