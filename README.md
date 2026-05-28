Data is the raw json file data 1 is the file after running cleaning.py which includes
Remove users with missing names.
Remove duplicate friend entries.
Remove inactive users (users with no friends and no liked pages).
duplicate pages based on IDs.

Then the recommendation.py file recommends users based on the friends of the given user, if A knows B and B knows C there is a high chance A knows C thats the algorithm ran for every friend of a given user.

Lastly running pages_you_may_like.py we use collaborative filtering to recommend the user pages in order of probability that he might like it.


How 'Pages You Might Like' Works:
Users engage with pages (like, comment, share, etc.).
If two users have interacted with similar pages, they are likely to have common interests.
For the sake of this implementation, we consider liking a page as an interaction
Pages followed by similar users should be recommended.
Example:

Amit (ID: 1) likes Python Hub (Page ID: 101) and AI World (Page ID: 102).
Priya (ID: 2) likes AI World (Page ID: 102) and Data Science Daily (Page ID: 103).
Since Amit and Priya both like AI World (102), we suggest Data Science Daily (103) to Amit and Python Hub (101) to Priya.
What we are using here is called collaborative filtering:

"If two people like the same thing, maybe they’ll like other things each one likes too."

This is a basic form of a real-world recommendation engine, and our task is to implement it in pure Python. 

Algorithm
We'll create a function that:

Maps users to pages they have interacted with.
Identifies pages liked by users with similar interests.
Ranks recommendations based on common interactions.






