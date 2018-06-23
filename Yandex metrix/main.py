from urllib.parse import urlencode
import requests
APP_ID = '09021915717b456e953120f15d851043'
AUTH_URL = 'https://oauth.yandex.ru/authorize'
REPORT_URL = 'https://api-metrika.yandex.ru/stat/v1/data'
COUNTER_ID = 49331800
TOKEN = 'AQAAAAADsldgAAUSwTw0NI5tq0Nskoj4c6XUy0A'


class YaMetrikaReport:
    metrics = ['ym:s:visits', 'ym:s:users', 'ym:s:pageviews']

    def __init__(self, token):
        self.token = token

    def get_report(self):
        report_data = dict(
            metrics=','.join(self.metrics),
            id=COUNTER_ID,
            oauth_token=self.token
        )
        req = '?'.join((REPORT_URL, urlencode(report_data)))
        result = requests.get(req)
        return result.json()['totals']


stat_params = YaMetrikaReport(TOKEN)
print('Визиты: {0[0]},\nПосетители:{0[1]}\nПросмотры:{0[2]}'.format(stat_params.get_report()))
