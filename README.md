# Dice Roller

This is a simple dice rolling program without GUI. All info and feedback are outputted through .print() method.

Good for python newcomers, because I am explaining in details how it works and all concepts involved in it.

---

## First Steps

You will not need any IDE or even Python installed. All is available in [Google Colab](https://colab.research.google.com/).

Access this `TODO:` [link](https://) and the program will be runnable.

---

## Code Overview

### main

This class is where it all begins. It creates a `Board` and call its functions.

### Board

This object is responsible for calling the `dice` functions. It also stores the dices.

When created, it will ask `how many dices the user wants`.

Then, it will guide the creation of specific types of dices until there is none left.

Finally, it will roll those dices created.

If the dice is one of the preset types, it's print will be custom.

---


[re.fullmatch()](https://docs.python.org/3/library/re.html#re.fullmatch)

