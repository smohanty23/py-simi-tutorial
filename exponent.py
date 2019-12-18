secret_word = "giraffe"
guess=""
limit=3
num_tries=0
out_of_guesses = False
while guess!=secret_word and not(out_of_guesses):
    if num_tries<limit :
        guess=input("Enter guess : ")
        num_tries+=1
    else:
        out_of_guesses = True
if out_of_guesses:
    print ("You Lose")
else:
    print ("You Win")

