Data is the raw json file data 1 is the file after running cleaning.py which includes
Remove users with missing names.
Remove duplicate friend entries.
Remove inactive users (users with no friends and no liked pages).
duplicate pages based on IDs.

Then the recommendation.py file recommends users based on the friends of the given user, if A knows B and B knows C there is a high chance A knows C thats the algorithm ran for every friend of a given user.






