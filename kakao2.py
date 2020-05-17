import sys
import numpy as np
import pandas as pd


# def cosine_similiarity(user):
#     for n in range(num_items):
#         if arr[users]

input = sys.stdin.readline
num_sim_user_topk = int(input())
num_item_rec_topk = int(input())
num_users = int(input())
num_items = int(input())
arr = [[False]* (num_items +1) for _ in range(num_users +1)]

for items in range(num_items):
    user, item, score = map(int, input().split())
    arr[user][items] = score

for user in range(num_users):
    df = pd.DataFrame(user, arr[user])

num_reco_users = int(input())
user1 = int(input())
user2 = int(input())
print(df)