n = int(input())

player = list(map(int, input().split()))
shuffle = list(map(int, input().split()))

card = list(range(n))
original = card[:]

end = True
for i in range(n):
    if player[card[i]] != i % 3:
        end = False
        break

if end:
    print(0)
    exit()

cnt = 0

while True:

    new_cards = [0] * n
    for i in range(n):
        new_cards[shuffle[i]] = card[i]
    card = new_cards
    cnt += 1

    end = True
    for i in range(n):
        if player[card[i]] != i % 3:
            end = False
            break

    if end:
        print(cnt)
        break

    if card == original:
        print(-1)
        break

