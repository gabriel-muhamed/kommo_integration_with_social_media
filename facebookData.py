## Facebook
import requests

access_token = 'EAAbZBHTyNBT0BOzjK2OlWDbFbJAujCoCvd7czdQo9JIZCmerGM21eVNZBPCiQm2gbktlZBw0gdHA4m0kKtvHqUZB6AtlAPkspFZAqrd7KuH1s0eTdW38aU64rZCWWOERobM8pzfwPmJw80KS89UoEBMLltVWmGU5zHyAZCS6KDh7SK7D90rXA9rjzweO'
facebook_page_id = '103191527799413'
base_url = 'https://graph.facebook.com/v20.0'

# Função para obter seguidores e nome da página do Facebook
def get_facebook_page_info(facebook_page_id, access_token):
    endpoint = f'{base_url}/{facebook_page_id}'
    params = {
        'fields': 'name,followers_count',
        'access_token': access_token
    }
    response = requests.get(endpoint, params=params)
    return response.json()

# Função para obter alcance da página do Facebook
def get_facebook_insights(facebook_page_id, access_token):
    endpoint = f'{base_url}/{facebook_page_id}/insights'
    params = {
        'metric': 'page_impressions,page_engaged_users',
        'period': 'days_28',
        'access_token': access_token
    }
    response = requests.get(endpoint, params=params)
    return response.json()

# Função para obter interações nas publicações da página do Facebook
def get_facebook_post_insights(facebook_page_id, access_token):
    endpoint = f'{base_url}/{facebook_page_id}/posts'
    params = {
        'fields': 'id,message,likes.summary(true),comments.summary(true)',
        'access_token': access_token
    }
    response = requests.get(endpoint, params=params)
    return response.json()

# Função para organizar e exibir os dados
def print_formatted_data(page_info, page_insights, post_insights):
    print("Dados Facebook")

    # Nome da página
    print(f"Nome da página: {page_info.get('name', 'N/A')}")

    # Seguidores
    print(f"Total de seguidores: {page_info.get('followers_count', 'N/A')}")

    # Interações
    total_likes = 0
    total_comments = 0
    for post in post_insights.get('data', []):
        total_likes += post['likes']['summary']['total_count']
        total_comments += post['comments']['summary']['total_count']

    print(f"Interações: {total_likes + total_comments}")

    # Alcance
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

    # Separação das informações
    print("==============================================================")

page_info = get_facebook_page_info(facebook_page_id, access_token)
page_insights = get_facebook_insights(facebook_page_id, access_token)
post_insights = get_facebook_post_insights(facebook_page_id, access_token)

print_formatted_data(page_info, page_insights, post_insights)