import requests
import pandas as pd

def get_requests(link):
    '''
    requesting data from API
    Args:
        link: API link
    Returns:
        Dictionary: requested data
    '''
    response = requests.get(link)
    return response.json()


def get_simple_json(body):
    '''
    simplify json format by extracting only needed information by prefecture
    Args:
        body: json object for each prefecture
        overall_stats: dictionary to store all covid19 information
    '''
    temp_prefecture_stats = []


    for i in range(len(body)):
        int_date = body[i]['last_updated']['cases_date']
        prefecture = body[i]['name_ja']
        population = body[i]['population']
        cases = body[i]['cases']
        deaths = body[i]['deaths']

        temp_prefecture_stats.append({
                "prefecture": prefecture,
                "population": population,
                "cases": cases,
                "deaths": deaths

        })

    overall_stats = {
        "date": int_date,
        "stats": temp_prefecture_stats
    }
    return overall_stats
