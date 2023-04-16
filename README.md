# IWANNADIE
<a href = "https://github.com/AntikoreDev/IWANNADIE" onClick = "return false"><img alt = "Repo size" src = "https://img.shields.io/github/repo-size/AntikoreDev/IWANNADIE"></a>
<a href = "https://github.com/AntikoreDev/IWANNADIE/pulls"><img alt = "Pull Requests" src = "https://img.shields.io/github/issues-pr/AntikoreDev/IWANNADIE"></a>
<a href = "https://github.com/AntikoreDev/IWANNADIE/graphs/contributors"><img alt = "Contributors" src = "https://img.shields.io/github/contributors/AntikoreDev/IWANNADIE"></a>
<a href = "https://github.com/AntikoreDev/IWANNADIE/stargazers"><img alt = "Stars" src = "https://img.shields.io/github/stars/AntikoreDev/IWANNADIE"></a>
<a href = "https://github.com/AntikoreDev/IWANNADIE/blob/main/LICENSE"><img alt = "License" src = "https://img.shields.io/github/license/AntikoreDev/IWANNADIE"></a>

<img src="https://www.antikore.dev/img/iwd.png" alt="IWANNADIE logo" style="float:right" width="128" height="128">
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

|Command     |Arguments   |Description |Returns     |
|:-----------|:-----------|:-----------|:-----------|
|print       |string      |Prints the string to the terminal|null|
|input       |string      |Prints the string to the terminal and waits the user for inputs|string|
|set         |symbol, any |Sets that symbol to the value provided as second argument|null|
|add         |symbol/any, any |Adds two values together, returns the result. If the first argument is a symbol, it will add the value to it too|real|
|mul         |symbol/any, any |Multiply two values together, returns the result. If the first argument is a symbol, it will multiply the value over it too|real|
|div         |symbol/any, any |Divide two values together, returns the result. If the first argument is a symbol, it will divide the value from it too|real|
|mod         |symbol/any, any |You get to the point right?|real|
|time        |-|Current time as of UNIX system|real|
|int         |any|Converts a value into int|int|
|real        |any|Converts a value into real|real|
|floor       |any|Floors the value|real|
|round       |any|Rounds the value|real|
|text        |string, string|Concatenates two strings together|string|
|check       |any, any|Returns true if both arguments are equal|boolean|
|not         |boolean|Negates the equivalent boolean of the first argument|boolean|
|or          |boolean, boolean|Returns true if any of the two arguments is true|boolean|
|and         |boolean, boolean|Returns true if both of the two arguments are true|boolean|
|comp/compare|any, any|Returns true whether the first argument is bigger than the latter|boolean|
|goto        |string|Moves the execution cursor to the tag named as the string passeed as argument|null|
|goif        |string, boolean|Moves the execution cursor to the tag named as the string passeed as argument only if the boolean passed in the second argument is true, otherwise it will continue as normal|null|
|doif        |boolean|Skips the following line of the script whether the boolean passed as argument is false|null|
|char/at     |string, int|Returns the character at the int argument on the arugment string|string|
|lambda/fn   |string, script|Define a lambda function|null|
|run         |string, args...|Runs a lambda function that has the string as name, using the arguments. Returns the returnal of the lambda function|any|
|random      |real, real|Returns a random floating point number between first and second argument|real|
|len         |string|Returns the length of the string passed as argument|real|
|clear       |-|Clears the output|null|
|die         |-|Kills the script and terminates execution|null|

## Donations
You can always support my work and effort by [buying me a coffee](https://ko-fi.com/antikore) 
