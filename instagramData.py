## Instagram
import requests
import json

access_token = ''
base_url = 'https://graph.facebook.com/v20.0'
instagram_account_id = ''

## Function to get Instagram account followers and user
def get_instagram_account_info(instagram_account_id, access_token):
    endpoint = f'{base_url}/{instagram_account_id}'
    params = {
        'fields': 'username, followers_count',
        'access_token': access_token
    }
    response = requests.get(endpoint, params=params)
    return response.json()

## Function to get Instagram account reach
def get_instagram_insights(instagram_account_id, access_token):
    endpoint = f'{base_url}/{instagram_account_id}/insights'
    params = {
        'metric': 'reach',
        'period': 'days_28',
        'access_token': access_token
    }
    response = requests.get(endpoint, params=params)
    return response.json()

# Function to get Instagram media insights
def get_instagram_media_insights(instagram_account_id, access_token):
    endpoint = f'{base_url}/{instagram_account_id}/media'
    params = {
        'fields': 'id,caption,like_count,comments_count',
        'access_token': access_token
    }
    response = requests.get(endpoint, params=params)
    return response.json()

# Function to organize and display the data
def create_json_file(account_info, account_insights, media_insights, filename='instagram_data.json'):
    # Obter o número total de interações
    total_interactions = sum(media['like_count'] + media['comments_count'] for media in media_insights.get('data', []))
    
    # Obter o total de alcance
    reach = 0
    for insight in account_insights.get('data', []):
        if insight['name'] == 'reach':
            for value in insight.get('values', []):
                reach += value.get('value', 0)
    
    data = {
        "Instagram Data": {
            "Username": account_info.get('username', ''),
            "TotalFollowers": account_info.get('followers_count', 0),
            "Interactions": total_interactions,
            "Reach": reach
        }
    }

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

account_info = get_instagram_account_info(instagram_account_id, access_token)
account_insights = get_instagram_insights(instagram_account_id, access_token)
media_insights = get_instagram_media_insights(instagram_account_id, access_token)

create_json_file(account_info, account_insights, media_insights)
