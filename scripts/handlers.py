import os
import re
import sys

import django

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "freeze.settings")
django.setup()

from funds.models import Fund


def handle_fund_code():
    path = os.path.join(os.path.join(BASE_DIR, 'static'), 'data')
    with open(os.path.join(path, 'fund_code.txt'), 'r', encoding='utf-8') as f:
        fund_codes = f.read()

    fund_codes = fund_codes[10:-3]
    fund_codes = fund_codes.split('],[')

    pattern = re.compile(r'"(.*?)"')
    for original_fund_code in fund_codes:
        fund = pattern.findall(original_fund_code)
        try:
            Fund.objects.create(code=fund[0],
                                brief=fund[1],
                                name=fund[2],
                                type=fund[3])
        except Exception as e:
            print(e, fund)

if __name__ == '__main__':
    handle_fund_code()