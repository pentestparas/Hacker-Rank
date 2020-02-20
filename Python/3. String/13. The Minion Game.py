def minion_game(string):
    vowels = 'AEIOU'
    sl = len(string)
    kevin_score, stuart_score = 0, 0

    for i in range(sl):
        if s[i] in vowels:
            kevin_score += (sl - i)
        else:
            stuart_score += (sl - i)

    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif kevin_score < stuart_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)