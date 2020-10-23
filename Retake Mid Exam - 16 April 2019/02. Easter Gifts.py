gifts = input().split()



while True:
    command = input()
    if command == 'No Money':
        break

    if command.startswith('OutOfStock'):
        _, gift = command.split()
        if gift in gifts:
            gifts = [i.replace(gift, 'None') for i in gifts]


    elif command.startswith('Required'):
        _, gift, sindex = command.split()
        sindex = int(sindex)
        if sindex in range(len(gifts)):
            gifts[sindex] = gift

    elif command.startswith('JustInCase'):
        _, gift = command.split()
        gifts[-1] = gift


print(" ".join([g for g in gifts if g != 'None']))



'''
Create a program that helps you plan the gifts for your friends and family. First, you are going to receive the gifts you plan on buying оn a single line, separated by space, in the following format:
"{gift1} {gift2} {gift3}… {giftn}"
Then you will start receiving commands until you read the "No Money" message. There are three possible commands:
    • "OutOfStock {gift}"
        ◦ Find the gifts with this name in your collection, if there are any, and change their values to "None".  
    • "Required {gift} {index}"
        ◦ Replace the value of the current gift on the given index with this gift, if the index is valid. 
    • "JustInCase {gift}"
        ◦ Replace the value of your last gift with this one. 
In the end, print the gifts on a single line, except the ones with value "None", separated by a single space in the following format:
"{gift1} {gift2} {gift3}… {giftn}"'''