import requests


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


def get_json_by_prefecture(body):
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
                "deaths": deaths,
                "cases_per_population": cases*100/population,
                "deaths_per_population": deaths*100/population,

        })

    overall_stats = {
        "date": int_date,
        "stats": temp_prefecture_stats
    }
    return overall_stats



def get_json_total_stats(body):

    temp_total_stats = []

    for i in range(len(body)):
        date = body[i]['date']
        pcr_cases = body[i]['pcr']
        positive = body[i]['positive']
        severe = body[i]['severe']
        death = body[i]['death']
        deaths_rate = body[i]['death'] * 100 / (body[i]['positive'] + 1)

        temp_total_stats.append({
            "date": date,
            "pcr_cases": pcr_cases,
            "positive": positive,
            "severe": severe,
            "death": death,
            "deaths_rate": deaths_rate

        })

        overall_stats = {
            "stats": temp_total_stats
        }
    return overall_stats

# by_prefecture_request = get_requests('https://covid19-japan-web-api.now.sh/api/v1/prefectures')
# total_stats_request = get_requests('https://covid19-japan-web-api.now.sh/api/v1/total?history=true')
#
# daily_stats_by_prefecture = get_json_by_prefecture(by_prefecture_request)
# print(len(daily_stats_by_prefecture.keys()))
# total_stats = get_json_total_stats(total_stats_request)
# print(len(total_stats.keys()))
# print(len(total_stats['stats']))
# print(total_stats)