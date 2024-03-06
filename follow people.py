from start import *
start()

#------------------------------FOLLOW PEOPLE ------------------------------

#choose a random brand and find its user id and attach it to "account id"
## THis is just some random accounts that i used to follow people for my bot
brands = ["__heavencanwait__", "thoughtwefriends", "namedcollective" ,"racerworldwide","urbansophisticationtm"]
random_brand = random.choice(brands)
print(f"Brand chosen: {random_brand}")
account_id = client.user_id_from_username(random_brand)


#this will pick up the followers information (all of it)
#gql = public

f_ammount = int(input("How many accounts do you want to follow:"))

followers = client.user_followers_gql(account_id, f_ammount)

for i , media in enumerate(followers):
    client.user_follow(media.pk)
    print(f"Followed user {i+1}: {media.username}")





