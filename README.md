- Scrapping the data
    - got the user_id from https://api.github.com/search/users?q=location:Barcelona+followers:>100
    - for each user made separate request to fetch user and repo details
    - for individual user details used https://api.github.com/users/{user_id}
    - for repos for each user https://api.github.com/users/{user_id}/repos?sort=pushed&direction=desc

- Interesting and surprising facts

- Recommendation
