import random
score = 0
car_position=random.randint(1,3)

print(" CAR RACING GAME")
print("A = Left, D = Right, Q = Quit , AA= 3 to 1 , DD= 1 to 3")

while True:
    enemy_position=random.randint(1,3)

    print("\n Road: [1][2][3]")
    print("Enemy:", enemy_position)
    print("Your car:", car_position)

    if enemy_position == car_position:
        print(" game over!")
        print("Score=", score)
        break

    move = input("Move: ").lower()

    ## Left boundary  ##
    if move == "a" and car_position == 1:
        print(" game over! You crossed the left boundary.")
        print("score=", score)
        break

    ## Right boundary    ##
    if move == "d" and car_position == 3:
        print(" game over! You crossed the right boundary.")
        print("score=", score)
        break

    if move == "a" and car_position > 1:
        car_position -= 1
    elif move == "d" and car_position < 3:
        car_position += 1
    elif move =="dd" and car_position ==1:
        car_position=3
    elif move =="aa" and car_position==3:
        car_position=1        
    elif move == "q":
        print("Game ended.")
        print("score=", score)
        break

    score += 1
