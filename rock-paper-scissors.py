import random

hands = ['グー', 'チョキ', 'パー']

def start_battle(player_hand):
  enemy_hand = random.randint(0, 3)
  print('相手は' + hands[enemy_hand] + 'を出しました')
  if player_hand == enemy_hand:
    print('引き分けです')
    return

print('グー : 0, チョキ : 1, パー : 2')
player_hand = int(input('出す手を入力 : '))
print('あなたは' + hands(player_hand) + 'を出しました')
start_battle(player_hand)
