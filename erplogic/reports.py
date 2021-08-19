from django.utils.translation import ugettext_lazy as _
from ra.reporting.registry import register_report_view
from ra.reporting.views import ReportView
from .models import Client, SalesLineTransaction, Product


@register_report_view
class ClientTotalBalance(ReportView):
    report_title = _('Clients Balances')

    base_model = Client
    report_model = SalesLineTransaction

    group_by = 'client'
    columns = ['slug', 'title', '__balance__']

    chart_settings = [
        {
            'id': 'pie_chart',
            'type': 'pie',
            'title': _('Client Balances'),
            'data_source': ['__balance__'],
            'title_source': 'title',
        },
        {
            'id': 'bar_chart',
            'type': 'bar',
            'title': _('Client Balances [Bar]'),
            'data_source': ['__balance__'],
            'title_source': 'title',
        },
    ]

@register_report_view
class ProductTotalSales(ReportView):
    # Title will be displayed on menus, on page header etc...
    report_title = _('Product Sales')

    # What model is this report about
    base_model = Product

    # What model hold the data that we want to compute.
    report_model = SalesLineTransaction

    # The meat and potato of the report.
    # We group the records in SimpleSales by Client ,
    # And we display the columns `slug` and `title` (relative to the `base_model` defined above)
    # the magic field `__balance__` computes the balance (of the base model)
    group_by = 'product'
    columns = ['slug', 'title', '__balance_quantity__']

@register_report_view
class ClientDetailedStatement(ReportView):
    report_title = _('client Statement')
    base_model = Client
    report_model = SalesLineTransaction


    columns = ['slug', 'doc_date', 'doc_type', 'product__title', 'quantity', 'price', 'value']


@register_report_view
class ProductSalesMonthly(ReportView):
    report_title = _('Product Sales Monthly')

    base_model = Product
    report_model = SalesLineTransaction

    group_by ='product'
    columns = ['slug', 'title']

        # how we made the report a time series report
    time_series_pattern = 'monthly'
    time_series_columns = ['__balance__']

    chart_settings = [
        {
            'id': 'movement_column_ns',
            'title': _('comparison - Column'),
            'data_source': ['__balance__'],
            'title_source': ['title'],
            'type': 'column',
        },
        {
            'id': 'movement_bar',
            'title': _('comparison - Column - Stacked'),
            'data_source': ['__balance__'],
            'title_source': ['title'],
            'type': 'column',
            # 'stacked': True,
            'stacking': 'normal',
        },
        {
            'id': 'movement_column_total',
            'title': _('comparison - Column - Total'),
            'data_source': ['__balance__', '__balance_quantity__'],
            'title_source': ['title'],
            'type': 'column',
            'plot_total': True,
        },
        {
            'id': 'movement_line',
            'title': _('comparison - line'),
            'data_source': ['__balance__'],
            'title_source': ['title'],
            'type': 'line',
        },
        {
            'id': 'movement_line_stacked',
            'title': _('comparison - Area - Stacked-Percent'),
            'data_source': ['__balance__'],
            'title_source': ['title'],
            'type': 'area',
            'stacking': 'percent',
        },
        {
            'id': 'movement_line_total',
            'title': _('comparison - line - Total'),
            'data_source': ['__balance__'],
            'title_source': ['title'],
            'type': 'line',
            'plot_total': True,
        },
    ]

@register_report_view
class ClientSalesMonthlySeries(ReportView):
    report_title = _('Client Sales Monthly')

    base_model = Client
    report_model = SalesLineTransaction


    group_by = 'client'
    columns = ['slug', 'title']

    time_series_pattern = 'monthly'
    time_series_columns = ['__total__']

@register_report_view
class ProductClientSalesCrosstab(ReportView):
    base_model = Product
    report_model = SalesLineTransaction
    report_title = _('Product Client sales Cross-tab')

    group_by = 'product'
    columns = ['slug', 'title']

    # cross tab settings
    crosstab_model = 'client'
    crosstab_columns = ['__total__']

    chart_settings = [
        {
            'type': 'column',
            'data_source': ['__total__'],
            'plot_total': False,
            'title_source': 'title',
            'title': _('Detailed Columns'),

        },
        {
            'type': 'column',
            'data_source': ['__total__'],
            'plot_total': False,
            'title_source': 'title',
            'stacking': 'normal',
            'title': _('Stacked Columns'),

        },
        {
            'type': 'pie',
            'data_source': ['__total__'],
            'plot_total': True,
            'title_source': 'title',
            'title': _('Total Pie'),

        }
    ]

