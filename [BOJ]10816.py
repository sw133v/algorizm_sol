from collections import defaultdict
def sol_10816():
    deck = defaultdict(int)
    first_deck_len = int(input())
    first_deck = list(map(int, input().split()))
    for i in range(first_deck_len):
        deck[first_deck[i]] += 1

    second_deck_len = int(input())
    second_deck = list(map(int, input().split()))
    res = [deck[second_deck[i]] for i in range(second_deck_len)]
    
    print(*res)

sol_10816()