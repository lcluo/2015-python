'''
A simple client for USDA statistics
    http://quickstats.nass.usda.gov/api

Found the data set in the data.gov catalog:
    http://catalog.data.gov/dataset/quick-stats-agricultural-database-api

Fun fact: This actually queries a database with 31 million records
'''

import requests


# You'll need to change this to the key from the email
usda_key = "A92362AA-3706-3CCC-859D-95A3A2A2E89C"

# If you save this publicly to Github then it's better to keep your key in
# a separate private plain text file called 'usda_key.txt'
try:
    with open('usda_key.txt') as f:
        usda_key = f.read().rstrip()
except FileNotFoundError:
    pass


def get_param_values(param, key=usda_key):
    '''
    Returns the possible values for a single parameter 'param'

    >>> get_param_values('sector_desc')[:3]
    ['ANIMALS & PRODUCTS', 'CROPS', 'DEMOGRAPHICS']

    '''
    # Your task- fill this in
    base = "http://quickstats.nass.usda.gov/api/get_param_values/?key=" + usda_key + "&param=" + param + "&format=JSON"
    response = requests.get(base)
    value = response.json()
    return value[param]   
    pass

def query(parameters, key=usda_key):
    '''
    Returns the JSON response from the USDA agricultural database

    'parameters' is a dictionary of parameters that can be referenced here:
        http://quickstats.nass.usda.gov/api

    Example: Return all the records around cattle in Tehama County

    >>> cowparams = {'commodity_desc': 'CATTLE',
                     'state_name': 'CALIFORNIA',
                     'county_name': 'TEHAMA'}
    >>> 

    '''
    # Your task- fill this in
    base = "http://quickstats.nass.usda.gov/api/api_GET/?key=" + usda_key
    response = requests.get(base, params = parameters)
    value = response.json()
    return value['data']
    pass


if __name__ == '__main__':
    # A few examples of usage

    # Possible values for 'commodity_desc'
    commodity_desc = get_param_values('commodity_desc')
    # Expect:
    # ['AG LAND', 'AG SERVICES', 'AG SERVICES & RENT',
    # 'ALMONDS', ...

    # Value of rice crops in Yolo (Davis) county since 2005
    riceparams = {'sector_desc': 'CROPS',
                  'commodity_desc': 'RICE',
                  'state_name': 'CALIFORNIA',
                  'county_name': 'YOLO',
                  'year__GE': '2005',
                  'unit_desc': '$',
                  }

    yolorice = query(riceparams)

tobaccoparams={'sector_desc': 'CROPS',
'commodity_desc': 'TOBACCO',
'year': '2012',
'agg_level_desc': 'STATE',
'statisticcat_desc': 'PRODUCTION',
'unit_desc': '$',
'reference_period_desc': 'YEAR',
'short_desc': 'TOBACCO - PRODUCTION, MEASURED IN $'
}

    # Try using a dictionary comprehension to filter
  #  yearvalue = {x['year']: x['Value'] for x in yolorice}
    # Expect:
    # {'2007': '26,697,000', '2012': '51,148,000'}
