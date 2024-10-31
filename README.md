## The Dataset is of Barcelona:100

- **Scrapping the data**
  
    - got the user_id from https://api.github.com/search/users?q=location:Barcelona+followers:>100
    - for each user made separate request to fetch user and repo details
    - for individual user details used https://api.github.com/users/{user_id} to fetch user specific data
    - for repos for each user used https://api.github.com/users/{user_id}/repos?sort=pushed&direction=desc
    - used python to handle data cleaning and applying constraints
    - refer **datascrapping.py** for code details

- **Interesting and surprising facts**
  
    - JavaScript and Python are among the most popular programming languages for these users which matches with the rest of the world
    - there is no significant correlation between no of followers and no of public repositories which means having more public repositories do not help in gaining followers
    - **MIT license** is the most popular license
    - Vim Script language has the highest average number of stars per repository which is surprising
    - Hireable people indeed follow more users which is expected
    - Almost half the users have no company information which could be an indication that most of the developers do not stay at a single comapny for longer period of time or do freelancing work mostly (as changing company name from time to time is slight hassle, so users avoid to put the information in the first place

- **Recommendation**
  
    - The whole analysis is done in google colab refer **tds-project1-23f1001897.ipynb** file for reference
    - a comparison of random users with barcelona users especially for correlation between followers and public repositories
    - for some questions the answer is null as null value frequency is high an analysis after removing those null values could be done 
