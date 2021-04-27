import random
import Score

shapes = ["H", "C", "S","D"]
cards = [[i, j ] for i in shapes for j in range(1,14)]
player1 = []
player2 = []
player3 = []

print(".********포커게임을시작합니다.********")
print("\n카드의표현은다음과같습니다\n")
formatted = format("Jack : 11", "<14s") + format("Queen : 12", "<14s") + format("King : 13", "<14s")
print(formatted) # item 4
print("\n점수는다음과같습니다.\n")

print("1. 스트레이트플러쉬\t:\t8점")
print("2. 포카드\t\t:\t7점")
print("3. 풀하우스\t\t:\t6점")
print("4. 플러쉬\t\t:\t5점")
print("5. 스트레이트\t\t:\t4점")
print("6. 트리플\t\t:\t3점")
print("7. 투페어\t\t:\t2점")
print("8. 원페어\t\t:\t1점")

print("\n플레이어들에게카드를나누어드립니다.\n")
random.shuffle(cards)
player1 = cards[:7]
player2 = cards[7:14]
player3 = cards[14:21]

formatted = format("You", "^24s") + format("computer1", "^24s") + format("computer2", "^24s")
print(formatted)
print("-"*72)
formatted = format("모양", "^10s") + format("숫자", "^10s")
print(formatted *3 )
table_string = ""
for i in range(7):
    for j in range(2):
        table_string += format(f"{player1[i][j]}", "^12s")
    for j in range(2):
        table_string += format(f"{player2[i][j]}", "^12s")
    for j in range(2):
        table_string += format(f"{player3[i][j]}", "^12s")
    print(table_string)
    table_string = ""

print("\n\n" + format('점수표', '^72s'))
print("-"*72)
formatted = format("You", "^24s") + format("computer1", "^24s") + format("computer2", "^24s")
print(formatted)
print("-"*72)
print(f"{Score.Score(player1):^24d}"+ f"{Score.Score(player2):^24d}" + f"{Score.Score(player3):^24d}")

