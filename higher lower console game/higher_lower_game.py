import random
from art import logo, vs
from game_data import data

def get_random_data():
    return random.choice(data)

def compare_data(acc_a, acc_b):
    if acc_a['follower_count'] > acc_b['follower_count']:
        return 'A'
    else:
        return 'B'

def get_new_account(acc_a):
    new_account = get_random_data()
    while new_account == acc_a:
        new_account = get_random_data()
    return new_account

score = 0

account_a = get_random_data()
account_b = get_new_account(account_a)

game_over = False
while not game_over:
    print("\n" * 100)
    print(logo)
    print(f"Current score: {score}")
    print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}")
    print(vs)
    print(f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    if guess == compare_data(account_a, account_b):
        score += 1
        account_a = account_b
        account_b = get_new_account(account_a)
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = True

