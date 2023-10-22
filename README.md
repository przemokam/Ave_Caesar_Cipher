# Ave_Caesar_Cipher
Caesar's cipher encoder / decoder / brute forcer

Link: [ave_caesar.py](https://github.com/przemokam/Ave_Caesar_Cipher/blob/main/ave_caesar.py)
```
      .o.       oooooo     oooo oooooooooooo                                           
     .888.       '888.     .8'  '888'     '8                                           
    .8"888.       '888.   .8'    888                                                   
   .8' '888.       '888. .8'     888oooo8                                              
  .88ooo8888.       '888.8'      888    "                                              
 .8'     '888.       '888'       888       o                                           
o88o     o8888o       '8'       o888ooooood8                                           
  .oooooo.         .o.       oooooooooooo  .oooooo..o       .o.       ooooooooo.   .o. 
 d8P'  'Y8b       .888.      '888'     '8 d8P'    'Y8      .888.      '888   'Y88. 888 
888              .8"888.      888         Y88bo.          .8"888.      888   .d88' 888 
888             .8' '888.     888oooo8     '"Y8888o.     .8' '888.     888ooo88P'  Y8P 
888            .88ooo8888.    888    "         '"Y88b   .88ooo8888.    888'88b.    '8' 
'88b    ooo   .8'     '888.   888       o oo     .d8P  .8'     '888.   888  '88b.  .o. 
 'Y8bood8P'  o88o     o8888o o888ooooood8 8""88888P'  o88o     o8888o o888o  o888o Y8P 
```

## Introduction

The Caesar Cipher is one of the earliest known and simplest ciphers. It is a type of substitution cipher in which each letter in the plaintext is shifted a certain number of places down or up the alphabet => **shift number**. 
For example, with a **shift** of 1, 'A' would be replaced by 'B', 'B' would become 'C', and so on. The method is named after Julius Caesar, who apparently used it to communicate with his generals.

![Caesar_cipher_left_shift_of_3 svg](https://github.com/przemokam/Ave_Caesar_Cipher/assets/124211669/776eeafa-f382-4516-9b1f-318dfbc9d832)

Example:
```
Plaintext:  THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
Ciphertext: QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD
```

## Features:
      
      There are 3 options to choose from:
          1. Decode a message when you know the shift number.
          2. Brute force decoding: if you don't know the shift number, the script will attempt all possible shifts for you.
          3. Encode a message by providing the desired shift number.

## How to Use

      Run the script using python.
      You'll be greeted with a choice of three actions:
          Decode message (I know shift)
          Decode message (I don't know the shift and I need to brute force it!)
          Encode message

      Depending on your choice, you might be prompted to input the message and possibly the shift number.
      The script will then display the encoded or decoded message based on your input.
      
      Thank you for using and testing the script!

## Credits

>This project was inspired by the 'Off-Platform Project: Coded Correspondence' exercise from Codecademy's Learn Python 3 Course.

