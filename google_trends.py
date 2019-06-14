from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US',tz=360)
kw_list = ["Blockchain"]
pytrends.build_payload(kw_list, cat=0, timefrrame='today 5-y', geo='', gprop='')
df = pytrends.interest_over_time(kw_list)
df = pytrends.interest_over_time()
pytrends.get_historical_interest(kw_list,year_start=2019,month_start=5, day_start=1, hour_start=0, year_end=2019, month_end=5, day_end=10, hour_end=24, cat=0, geo='', gprop='', sleep=0)
