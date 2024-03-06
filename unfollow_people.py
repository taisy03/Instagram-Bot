import pip
import random 
import maskpass

from start import *
start()


users = client.user_following(client.user_id).keys()
print(f"Users following: {len(users)}")
numb_of_users = int(input("How many people to unfollow: "))
users_still_following = len(users) - numb_of_users


for i , user in enumerate(users):
        if i > numb_of_users - 1 :
                print(f'Users still following : {users_still_following}')
                break
        else:
                client.user_unfollow(user)        
                print(f"Unfollowed user {i+1} : {client.username_from_user_id(user)}")

