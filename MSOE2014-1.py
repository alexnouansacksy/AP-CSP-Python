def main():
    word = input("Enter a word: ")
    word = word.lower()
    dblcount = 0
    for i in range(0, len(word)-1):
        if word[i] == word[i+1]:
            dblcount += 1
    print(f"The word '{word}' contains {dblcount} double letters")
    pass

if __name__ == "__main__":
    main()

'''
Enter a word: miSSisSiPpI
The word 'mississippi' contains 3 double letters
'''