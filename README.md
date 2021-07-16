# Twitter Replication 

submitted by: **Davis Tran**
pennkey: **davisdt**

## how to run the amazing tumblr recreation 

**1)** cd into the twitter directory
**2)** pip install -r requirements.txt
**3)** on the command line, run "python manage.py makemigrations" 
**4)** on the command line, run "python manage.py migrate" 
**5)** on the command line, run "python manage.py runserver" 
**6)** should be on localhost:8000 -- enjoy

## routes
- /admin | django admin portal
- / | splash page, explanation of this twitter
- /login | login, signup page
- /profile/< username > | username's profile page with their tweets
- /home | home page with all tweets and hashtags
- /hashtag | page with all hashtags 
- /hashtag< hashtag > | page with all tweets with a particular hashtag

## design considerations
- used a ManyToMany relationship where tweets can have many hashtags.
- allowed users to delete their own tweets from any page as well as like any post at most once
- hashtags page shows all the hashtags and clicking on one lists all the tweets with that particular hashtag