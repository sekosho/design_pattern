from random import randint


def generate_enemy_hand():
    while True:
        yield "1"
        yield "2"
        yield "3"


def is_win(my_hand, enemy_hand):
    if any(
        [
            (my_hand == "1" and enemy_hand == "2"),
            (my_hand == "2" and enemy_hand == "3"),
            (my_hand == "3" and enemy_hand == "1"),
        ]
    ):
        return True
    return False


hands_dict = {"1": "グー", "2": "チョキ", "3": "パー"}


gen = generate_enemy_hand()
count_lose = 0
while True:
    your_hand = input("ジャンケンポン!!数字で入力ください。\n 1:グー、2:チョキ、3:パー：")
    if your_hand not in ["1", "2", "3"]:
        print("再入力してください")
        continue
    # enemy_hand = str(randint(1, 3))
    enemy_hand = next(gen)

    print(f"あなたの出した手:{hands_dict[your_hand]}、相手の出した手:{hands_dict[enemy_hand]}")
    if your_hand == enemy_hand:
        print("あいこ")
    elif is_win(your_hand, enemy_hand):
        print("あなたは勝ちました")
        break
    else:
        count_lose += 1
        if count_lose == 3:
            print("あなたは負けました")
            break
        else:
            print("あなたの負け、再チャレンジ")
