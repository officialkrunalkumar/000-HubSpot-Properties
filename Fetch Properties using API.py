import requests
import pandas as pd

# Set up the headers and API key
headers = {
    'Authorization': 'Bearer Your_API_KEY',
    'Content-Type': 'application/json'
}

# Function to fetch properties
def get_properties(object_type):
    url = f"https://api.hubapi.com/crm/v3/properties/{object_type}"
    response = requests.get(url, headers=headers)
    properties = response.json().get('results', [])
    return {prop['name']: prop for prop in properties}

# Fetch contact and company properties
contact_properties = get_properties('contact')
company_properties = get_properties('company')
deal_properties = get_properties('deal')

# Find common properties
common_properties_contact_company = set(contact_properties.keys()).intersection(company_properties.keys())
common_properties_contact_deal = set(contact_properties.keys()).intersection(deal_properties.keys())

print("Common properties between contact and company are :- ", len(common_properties_contact_company))
print(common_properties_contact_company)

print("Common properties between contact and deal are :- ", len(common_properties_contact_deal))
print(common_properties_contact_deal)

df = pd.DataFrame(common_properties_contact_company, columns=["Common properties Contact-Company"])
df.to_excel("contact-company.xlsx", index=False)

df = pd.DataFrame(common_properties_contact_deal, columns=["Common properties Contact-Deal"])
df.to_excel("contact-deal.xlsx", index=False)