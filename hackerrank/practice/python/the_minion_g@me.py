

##LOL i first tried to do it with subsets and that failed (miserably)
## then i picked up a pen and paper to do it "visually"
## and then i got it
##For the word "BANANA", 
##the first vowel 'A' occurs at position 1, len("BANANA") = 6, 
##so there are 6-1 = 5 substrings starting with this letter 'A': ['A', 'AN', 'ANA', 'ANAN', 'ANANA'], 
##you add one extra letter to that specific letter 'A' until you get to the end of the word.



def minion_game(string):
    sl = len(string)
    v = 0
    nv = 0
    data = []

    for index , i in enumerate(s):
        t = ''
        is_v = True if i in "AEIUO" else False
        if is_v:
            v += sl -index
        else:
            nv += sl-index

    if nv>v:
        print(f"Stuart {nv}")
    elif nv == v:
        print("Draw")
    else:
        print(f"Kevin {v}")
