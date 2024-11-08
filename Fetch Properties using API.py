import requests, os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('API_KEY')

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

def get_properties(object_type):
    url = f"https://api.hubapi.com/crm/v3/properties/{object_type}"
    response = requests.get(url, headers=headers)
    properties = response.json().get('results', [])
    return {prop['name']: prop for prop in properties}

contact_properties = get_properties('contact')
company_properties = get_properties('company')
deal_properties = get_properties('deal')

common_properties_contact_company = set(contact_properties.keys()).intersection(company_properties.keys())
common_properties_contact_deal = set(contact_properties.keys()).intersection(deal_properties.keys())

df = pd.DataFrame(common_properties_contact_company, columns=["Common properties Contact-Company"])
df.to_excel("contact-company.xlsx", index=False)

df = pd.DataFrame(common_properties_contact_deal, columns=["Common properties Contact-Deal"])
df.to_excel("contact-deal.xlsx", index=False)


quote_properties = get_properties('quote')
df = pd.DataFrame.from_dict(quote_properties, orient='index')
df.to_excel("quote.xlsx", index=False)

meeting_properties = get_properties('meeting')
df = pd.DataFrame.from_dict(meeting_properties, orient='index')
df.to_excel("meeting.xlsx", index=False)


def company_properties(object_type):
    url = f"https://api.hubapi.com/crm/v3/properties/{object_type}"
    params = {
        'include': 'extra_metadata'
    }
    response = requests.get(url, headers=headers, params=params)
    properties = response.json().get('results', [])
    return {prop['name']: prop for prop in properties}

companies_properties = company_properties('company')
df = pd.DataFrame.from_dict(meeting_properties, orient='index')
df.to_excel("company.xlsx", index=False)