import json
import facebookData  # Ajuste o nome do arquivo se necessário
import instagramData  # Ajuste o nome do arquivo se necessário

facebook_info = facebookData.get_facebook_page_info('103191527799413', 'YOUR_ACCESS_TOKEN')
facebook_insights = facebookData.get_facebook_insights('103191527799413', 'YOUR_ACCESS_TOKEN')
post_insights = facebookData.get_facebook_post_insights('103191527799413', 'YOUR_ACCESS_TOKEN')

instagram_info = instagramData.get_instagram_account_info('17841451238414172', 'YOUR_ACCESS_TOKEN')
instagram_insights = instagramData.get_instagram_insights('17841451238414172', 'YOUR_ACCESS_TOKEN')
media_insights = instagramData.get_instagram_media_insights('17841451238414172', 'YOUR_ACCESS_TOKEN')

data = {
    'facebook': {
        'followersCount': facebook_info['followers_count'],
        'totalLikes': sum(post['likes']['summary']['total_count'] for post in post_insights['data']),
        'totalComments': sum(post['comments']['summary']['total_count'] for post in post_insights['data']),
        'totalImpressions': sum(insight['values'][0]['value'] for insight in facebook_insights['data'] if insight['name'] == 'page_impressions')
    },
    'instagram': {
        'followersCount': instagram_info['followers_count'],
        'totalLikes': sum(media['like_count'] for media in media_insights['data']),
        'totalComments': sum(media['comments_count'] for media in media_insights['data']),
        'totalReach': sum(insight['values'][0]['value'] for insight in instagram_insights['data'] if insight['name'] == 'reach')
    }
}

with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)