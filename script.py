from stack import Stack

print("\nLet's play Towers of Hanoi!!")

# Create the Stacks
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)


# Set up the Game
num_disks = int(input("\nHow many dists do you want to play with?\n"))

while num_disks < 3:
    num_disks = int(input("Enter a number greater than or equal to 3\n"))

for i in range(num_disks, 0, -1):
    left_stack.push(i)

optimal_moves = 2**num_disks - 1
print("\nThe fastest you can solve this game is in {} moves".format(optimal_moves))

# Get User Input


def get_input():
    choices = [stack.get_name()[0] for stack in stacks]
    while True:
        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = choices[i]
            print("Enter {} for {}".format(letter, name))
        user_input = input("")
        if user_input in choices:
            for i in range(len(stacks)):
                if user_input is choices[i]:
                    return stacks[i]
        else:
            print("Please enter a valid choice")


# Play the Game
num_user_moves = 0
while right_stack.get_size() < num_disks:
    print("\n\n\n...Current Stacks...")
    for stack in stacks:
        stack.print_items()
    while True:
        flag = True
        from_stack, to_stack = None, None
        while flag:
            print("\nWhich stack do you want to move from?\n")
            from_stack = get_input()
            if from_stack.is_empty():
                print("\nInvalid Move; that stack is empty\nTry Again.")
            else:
                flag = False
        flag = True
        while flag:
            print("\nWhich stack do you want to move to?\n")
            to_stack = get_input()
            if not to_stack.is_empty() and to_stack.peek() < from_stack.peek():
                print("Invalid move; {} is larger than {}".format(
                    from_stack.peek(), to_stack.peek()))
            else:
                flag = False
        disk = from_stack.pop()
        to_stack.push(disk)
        num_user_moves += 1
        break
print("You took {} moves to complete this game!".format(num_user_moves))
if num_user_moves == optimal_moves:
    print("Congrats, that is the optimal number of moves! You played perfectly!")
else:
    print("Looks like you used more moves than necessary!")
