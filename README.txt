THIS PROJECT:
______________

This project models an ancient mathematical puzzle named "Towers of Hanoi". Please read the "Game Background" below for further elaboration about the rules and objectives of the game. 

While Towers of Hanoi is traditionally a physical game with tangible rods and disks, I decided to model this game in python using the stack data structure. The stack data structure is very fitting for this game, as it is designed with the purpose of only allowing access to most recently-added item in the stack, i.e. the "top-most" item in the stack. Similarly, the Towers of Hanoi game only grants access to the top-most disk of a given stack of disks on any particular rod. 



GAME BACKGROUND:
________________

Towers of Hanoi is an ancient mathematical puzzle that starts off with three rods situated adjacently, as well as many disks which successively decrease in size. The largest disk is placed at the bottom of the pile of disks while the smallest disk is placed on the top of the pile.

The objective of the game is to move all of the disks from the leftmost rod to the rightmost rod. The game follows three rules:

1. Only one disk can be moved at a time
2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
3. No disk may be placed on top of a smaller disk.
