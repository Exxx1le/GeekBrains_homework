import sys
from utils import currency_rates
import datetime

# print(currency_rates('USD'))
# print(currency_rates('EUR'))

currency = sys.argv[1]

print(f'{currency_rates(currency)}, {datetime.date.today()}')
