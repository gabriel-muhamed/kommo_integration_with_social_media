## Facebook
import requests

access_token = ''
facebook_page_id = ''
base_url = 'https://graph.facebook.com/v20.0'

# Function to get Facebook page followers and name
def get_facebook_page_info(facebook_page_id, access_token):
    endpoint = f'{base_url}/{facebook_page_id}'
    params = {
        'fields': 'name,followers_count',
        'access_token': access_token
    }
    response = requests.get(endpoint, params=params)
    return response.json()

# Function to get Facebook page reach
def get_facebook_insights(facebook_page_id, access_token):
    endpoint = f'{base_url}/{facebook_page_id}/insights'
    params = {
        'metric': 'page_impressions,page_engaged_users',
        'period': 'days_28',
        'access_token': access_token
    }
    response = requests.get(endpoint, params=params)
    return response.json()

# Function to get interactions on Facebook page posts
def get_facebook_post_insights(facebook_page_id, access_token):
    endpoint = f'{base_url}/{facebook_page_id}/posts'
    params = {
        'fields': 'id,message,likes.summary(true),comments.summary(true)',
        'access_token': access_token
    }
    response = requests.get(endpoint, params=params)
    return response.json()

# Function to organize and display data
def print_formatted_data(page_info, page_insights, post_insights):
    print("Dados Facebook")

    # Page Name
    print(f"Nome da página: {page_info.get('name', 'N/A')}")

    # Followers
    print(f"Total de seguidores: {page_info.get('followers_count', 'N/A')}")

    # Interactions
    total_likes = 0
    total_comments = 0
    for post in post_insights.get('data', []):
        total_likes += post['likes']['summary']['total_count']
        total_comments += post['comments']['summary']['total_count']

    print(f"Interações: {total_likes + total_comments}")

    # Reach
    total_impressions = 0
    total_engaged_users = 0
    for insight in page_insights.get('data', []):
        if insight['name'] == 'page_impressions':
            for value in insight['values']:
                total_impressions += value['value']
        elif insight['name'] == 'page_engaged_users':
            for value in insight['values']:
                total_engaged_users += value['value']

    print(f"Alcance: {total_impressions}")

page_info = get_facebook_page_info(facebook_page_id, access_token)
page_insights = get_facebook_insights(facebook_page_id, access_token)
post_insights = get_facebook_post_insights(facebook_page_id, access_token)

print_formatted_data(page_info, page_insights, post_insights)
