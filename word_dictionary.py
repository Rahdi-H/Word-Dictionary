def main():
    dictionary = {
        'Earth' : 'A planet',
        'Checken' : 'An Animal',
    }
    while True:
        word = input('Please enter the word?  ')
        if word not in dictionary or word == "":
            break
        if word in dictionary:
            print(word, ':', dictionary[word])

main()