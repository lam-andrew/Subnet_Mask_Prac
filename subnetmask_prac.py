# Program that will randomly generate CIDR notation subnet masks and prompt the user to enter the correct subnet mask in binary 
# Will randomly generate /8 - /32 

import random

print("\n\n\nThis Program will test your knowledge of CIDR Notation Subnet Masks. It will prompt you with the CIDR notation of the subnet mask and you must" +
      " answer with the correct binary subnet mask. Let's Begin.")

mask_count = 24 

mask = {1: '255.0.0.0', 2: '255.128.0.0', 3: '255.192.0.0', 4: '255.224.0.0', 5: '255.240.0.0', 6: '255.248.0.0', 7: '255.252.0.0', 8: '255.254.0.0', 9: '255.255.0.0', 
        10: '255.255.128.0', 11: '255.255.192.0', 12: '255.255.224.0', 13: '255.255.240.0', 14: '255.255.248.0', 15: '255.255.252.0', 16: '255.255.254.0', 17: '255.255.255.0', 
        18: '255.255.255.128', 19: '255.255.255.192', 20: '255.255.255.224', 21: '255.255.255.240', 22: '255.255.255.248', 23: '255.255.255.252', 
        24: '255.255.255.254', 25: '255.255.255.255'}

no_repitition = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}

# Continue until all is gone 
while mask_count > 0:

    repitition = True 

    # Get a random mask without repitition 
    while repitition == True: 
        current_num = int(random.uniform(1,25))    # return a number between (and included) 8 and 32 
        if current_num in no_repitition: 
            no_repitition.remove(current_num)
            current_mask = mask[current_num]
            display_num = current_num + 7
            repitition = False


    incorrect = True

    # Loop until user guesses correctly 
    while incorrect: 
        user_input = input("Return the binary mask of /" + str(display_num) + ": ")
        if(str(user_input) == current_mask):
            print("CORRECT!")
            incorrect = False
        else:
            print("INCORRECT. PLEASE TRY AGAIN")
            incorrect = True
        mask_count -= 1

print('\n\n\nYOU HAVE COMPLETED THE EXERCISE')