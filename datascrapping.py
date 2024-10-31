import requests
import pandas as pd
import json

api_token="my-secret"

# GitHub API URL
base_url = 'https://api.github.com'
headers = {'Authorization': f'token {api_token}'}

users_data=[]
page = 1
while True:
    users_url = f"{base_url}/search/users?q=location:Barcelona+followers:>100&page={page}&per_page=500"
    response = requests.get(users_url, headers=headers)
    data = response.json()

    if 'items' not in data or not data['items']:
        break
    users_data.extend(data['items'])
    page += 1

# Extract user info
users = []
for user in users_data:
    user_detail_url = user['url']
    user_response = requests.get(user_detail_url, headers=headers)
    user_info = user_response.json()

    # Clean up company name
    company = user_info.get('company', '')
    if company:
        company = company.strip().lstrip('@').upper()
    else:
        company = 'null'
    hireable = user_info.get('hireable', '')


    users.append({
        'login': user_info['login'],
        'name': user_info['name'],
        'company': company,
        'location': user_info['location'],
        'email': user_info['email'],
        'hireable': 'true' if user_info['hireable'] else 'false',
        'bio': user_info['bio'],
        'public_repos': user_info['public_repos'],
        'followers': user_info['followers'],
        'following': user_info['following'],
        'created_at': user_info['created_at']
        })

# Convert to DataFrame and save as CSV
users_df = pd.DataFrame(users)
users_df.to_csv('users.csv', index=False)

# Fetch repositories for each user
repos = []
for user in users:
    page = 1
    user_repos=[]
    while True:
        repos_url = f"{base_url}/users/{user['login']}/repos?sort=pushed&direction=desc&page={page}&per_page=100"
        # repos_url = f"{base_url}/users/{user['login']}/repos?per_page=100"
        repos_response = requests.get(repos_url, headers=headers)
        repos_data = repos_response.json()
        if not repos_data or len(user_repos) >= 500:
            break
        for repo in repos_data:
            if len(user_repos) >= 500:
                break
        # for repo in repos_data:
            user_repos.append({
                'login': user['login'],
                'full_name': repo['full_name'],
                'created_at': repo['created_at'],
                'stargazers_count': repo['stargazers_count'],
                'watchers_count': repo['watchers_count'],
                'language': repo['language'],
                'has_projects': 'true' if repo['has_projects'] else 'false',
                'has_wiki': 'true' if repo['has_wiki'] else 'false',
                'license_name': repo['license']['name'] if repo['license'] else 'null'
            })
        page+=1
    repos.extend(user_repos)

# Convert to DataFrame and save as CSV
repos_df = pd.DataFrame(repos)
repos_df.to_csv('repositories.csv', index=False)



print("Data scraping and file creation completed.")
users_df.shape
