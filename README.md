# IWANNADIE
**IWANNADIE** is an esoteric language made by me. This repository holds the v2 of the language adding new and interesting features. Scripts made in this language use the extension `.iwd`

This implemention could be named as IWANNADIE-23 or IWANNADIEEVENHARDER.
Original implementation from 2021 can be found here: IWANNADIE.py

## Examples

### [Hello, World!](https://esolangs.org/wiki/Hello,_world!)
```
print "Hello, World!"
die
```

### [Truth-Machine](https://esolangs.org/wiki/Truth-machine)
```
set #input, [input "Number >> "]
goif "zero", [check [add #input, 0], "0"]
@one
print "1"
goto "one"
@zero
print "0"
die
```

### [Factorial](https://esolangs.org/wiki/Factorial)
```
set #num, 5
set #org, [add #num, 0]
set #res, [add #num, 0]
@factorial
add #num, -1
mul #res, [add #num, 0]
goif "result", [check [add #num, 0], 1]
goto "factorial"
@result
print [text [int [add #org, 0]], [text " is ", [int [add #res, 0]]]]
die
```

### [FizzBuzz](https://esolangs.org/wiki/FizzBuzz)
```
set #counter, 0
@counter
add #counter, 1
goif "fizzbuzz", [and [check [mod [add #counter, 0], 3], 0], [check [mod [add #counter, 0], 5], 0]]
goif "fizz", [check [mod [add #counter, 0], 3], 0]
goif "buzz", [check [mod [add #counter, 0], 5], 0]
print [int [add #counter, 0]]
goto "repeat"
@fizz
print "Fizz"
goto "repeat"
@buzz
print "Buzz"
goto "repeat"
@fizzbuzz
print "FizzBuzz"
@repeat
goif "counter", [not [check [add #counter, 0], 100]]
die
```
### [99 bottles of beer](https://esolangs.org/wiki/99_bottles_of_beer)
```
set #bottles, 99
@alot
print " "
print [text [int [add #bottles, 0]], " bottles of beer on the wall"]
print [text [int [add #bottles, 0]], " bottles of beer"]
print "Take one down, pass it around"
add #bottles, -1
goif "one", [check [add #bottles, 0], 1]
print [text [int [add #bottles, 0]], " bottles of beer on the wall"]
goto "alot"
@one
print [text [int [add #bottles, 0]], " bottle of beer on the wall"]
print " "
print [text [int [add #bottles, 0]], " bottle of beer on the wall"]
print [text [int [add #bottles, 0]], " bottle of beer"]
print "Take one down, pass it around"
print "No bottles of beer on the wall."
die
```

## Commands
IWANNADIE scripts are constructed using concatenated commnads. This is the full list of usable commands

