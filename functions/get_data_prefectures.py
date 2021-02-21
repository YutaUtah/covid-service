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


def get_simple_json(body, overall_stats):
    '''
    simplify json format by extracting only needed information by prefecture
    Args:
        body: json object for each prefecture
        overall_stats: dictionary to store all covid19 information
    '''
    prefecture_stats = {

        "date": {
            "total": {
                "population": 0,
                "cases": 0,
                "deaths": 0
            }
        }
    }

    int_date = body['last_updated']['cases_date']
    s_date = pd.to_datetime(str(int_date), format='%Y%m%d')

    prefecture = body['name_ja']
    population = body['population']
    cases = body['cases']
    deaths = body['deaths']
    prefecture_stats.update({
        "date": s_date,
        "total": {
            "population": population,
            "cases": cases,
            "deaths": deaths
        }
    })

    overall_stats[prefecture] = prefecture_stats

