{"filter":false,"title":"lab17.py","tooltip":"/lab17.py","undoManager":{"mark":14,"position":14,"stack":[[{"start":{"row":0,"column":0},"end":{"row":55,"column":24},"action":"insert","lines":["# Module Lab: Caesar Cipher Program Bug #1","#","# In a previous lab, you created a Caesar cipher program. This version of","# the program is buggy. Use a debugger to find the bug and fix it.","","# Double the given alphabet","def getDoubleAlphabet(alphabet):","    doubleAlphabet = alphabet + alphabet","    return doubleAlphabet","","# Get a message to encrypt","def getMessage():","    stringToEncrypt = input(\"Please enter a message to encrypt: \")","    return stringToEncrypt","","# Get a cipher key","def getCipherKey():","    shiftAmount = input(\"Please enter a key (whole number from 1-25): \")","    return shiftAmount","","# Encrypt message","def encryptMessage(message, cipherKey, alphabet):","    encryptedMessage = \"\"","    uppercaseMessage = \"\"","    uppercaseMessage = message.upper()","    for currentCharacter in uppercaseMessage:","        position = alphabet.find(currentCharacter)","        newPosition = position + cipherKey","        if currentCharacter in alphabet:","            encryptedMessage = encryptedMessage + alphabet[newPosition]","        else:","            encryptedMessage = encryptedMessage + currentCharacter","    return encryptedMessage","","# Decrypt message","def decryptMessage(message, cipherKey, alphabet):","    decryptKey = -1 * int(cipherKey)","    return encryptMessage(message, decryptKey, alphabet)","","# Main program logic","def runCaesarCipherProgram():","    myAlphabet=\"ABCDEFGHIJKLMNOPQRSTUVWXYZ\"","    print(f'Alphabet: {myAlphabet}')","    myAlphabet2 = getDoubleAlphabet(myAlphabet)","    print(f'Alphabet2: {myAlphabet2}')","    myMessage = getMessage()","    print(myMessage)","    myCipherKey = getCipherKey()","    print(myCipherKey)","    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)","    print(f'Encrypted Message: {myEncryptedMessage}')","    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)","    print(f'Decrypted Message: {myDecryptedMessage}')","","# Main logic","runCaesarCipherProgram()"],"id":1}],[{"start":{"row":27,"column":33},"end":{"row":27,"column":34},"action":"insert","lines":["i"],"id":2},{"start":{"row":27,"column":34},"end":{"row":27,"column":35},"action":"insert","lines":["n"]},{"start":{"row":27,"column":35},"end":{"row":27,"column":36},"action":"insert","lines":["t"]},{"start":{"row":27,"column":36},"end":{"row":27,"column":37},"action":"insert","lines":["("]}],[{"start":{"row":27,"column":46},"end":{"row":27,"column":47},"action":"insert","lines":[")"],"id":3}],[{"start":{"row":27,"column":36},"end":{"row":27,"column":37},"action":"remove","lines":["("],"id":4},{"start":{"row":27,"column":35},"end":{"row":27,"column":36},"action":"remove","lines":["t"]},{"start":{"row":27,"column":34},"end":{"row":27,"column":35},"action":"remove","lines":["n"]},{"start":{"row":27,"column":33},"end":{"row":27,"column":34},"action":"remove","lines":["i"]}],[{"start":{"row":27,"column":42},"end":{"row":27,"column":43},"action":"remove","lines":[")"],"id":5}],[{"start":{"row":26,"column":50},"end":{"row":27,"column":0},"action":"insert","lines":["",""],"id":6},{"start":{"row":27,"column":0},"end":{"row":27,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":27,"column":8},"end":{"row":27,"column":9},"action":"insert","lines":["c"],"id":7},{"start":{"row":27,"column":9},"end":{"row":27,"column":10},"action":"insert","lines":["i"]},{"start":{"row":27,"column":10},"end":{"row":27,"column":11},"action":"insert","lines":["p"]},{"start":{"row":27,"column":11},"end":{"row":27,"column":12},"action":"insert","lines":["h"]},{"start":{"row":27,"column":12},"end":{"row":27,"column":13},"action":"insert","lines":["e"]},{"start":{"row":27,"column":13},"end":{"row":27,"column":14},"action":"insert","lines":["r"]}],[{"start":{"row":27,"column":8},"end":{"row":27,"column":14},"action":"remove","lines":["cipher"],"id":8},{"start":{"row":27,"column":8},"end":{"row":27,"column":17},"action":"insert","lines":["cipherKey"]}],[{"start":{"row":27,"column":17},"end":{"row":27,"column":18},"action":"insert","lines":[" "],"id":9},{"start":{"row":27,"column":18},"end":{"row":27,"column":19},"action":"insert","lines":["="]}],[{"start":{"row":27,"column":19},"end":{"row":27,"column":20},"action":"insert","lines":[" "],"id":10},{"start":{"row":27,"column":20},"end":{"row":27,"column":21},"action":"insert","lines":["i"]}],[{"start":{"row":27,"column":21},"end":{"row":27,"column":22},"action":"insert","lines":["n"],"id":11},{"start":{"row":27,"column":22},"end":{"row":27,"column":23},"action":"insert","lines":["t"]}],[{"start":{"row":27,"column":23},"end":{"row":27,"column":25},"action":"insert","lines":["()"],"id":12}],[{"start":{"row":27,"column":24},"end":{"row":27,"column":33},"action":"insert","lines":["cipherKey"],"id":13}],[{"start":{"row":13,"column":0},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":14},{"start":{"row":14,"column":0},"end":{"row":15,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":14,"column":0},"end":{"row":15,"column":0},"action":"remove","lines":["",""],"id":15},{"start":{"row":13,"column":0},"end":{"row":14,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":13,"column":0},"end":{"row":13,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1723727853035,"hash":"f57b9f5e0c7059d080d0b69281b88b5c9a10028a"}