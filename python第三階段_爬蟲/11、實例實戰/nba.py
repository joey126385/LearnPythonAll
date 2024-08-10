"""
https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season=2023-24&SeasonType=Playoffs&StatCategory=PTS
"""

import requests
import json
import os, xlwt, xlrd
from xlutils.copy import copy

headers = {
    # 'Accept': '*/*',
    # 'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'Connection': 'keep-alive',
    # 'Origin': 'https://www.nba.com',
    # 'Referer': 'https://www.nba.com/',
    # 'Sec-Fetch-Dest': 'empty',
    # 'Sec-Fetch-Mode': 'cors',
    # 'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    # 'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': '"Windows"',
}

params = {
    'LeagueID': '00',
    'PerMode': 'PerGame',
    'Scope': 'S',
    'Season': '2023-24',
    'SeasonType': 'Playoffs',
    'StatCategory': 'PTS',
}

def headers(h):
    print(len(h))

def data(d):
    print(d)


def main ():
    response = requests.get('https://stats.nba.com/stats/leagueLeaders', params=params, headers=headers)
    # print(response.text)
    result = json.loads(response.text)
    print(result["resultSet"]["headers"])  # 標題
    #  headers(result["resultSet"]["headers"])
    # data(result["resultSet"]["rowSet"])


main()