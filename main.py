def main():

    dice_A = [1,2,3,4,5,6]
    dice_B = [1,2,3,4,5,6]

    # PART A:
    total_combinations(dice_A, dice_B)
    probability_of_posible_sums(dice_A, dice_B)
    
    # PART B:    
    New_Die_A, New_Die_B = undoom_dice(dice_A, dice_B)
    print("New Dice A", New_Die_A, ", New Dice B", New_Die_B)
    probability_of_posible_sums(New_Die_A, New_Die_B)


def total_combinations(Die_A, Die_B):
    allCombinations=[]

    for i in range(len(Die_A)):
        for j in range(len(Die_B)):
            allCombinations.append([Die_A[i], Die_B[j]])
    
    print(allCombinations)
    
    print("There are a total ", len(allCombinations), " possible combination")
    print("6 sided die X 6 sided die = ", len(allCombinations))


def probability_of_posible_sums(Die_A, Die_B):

    total_possibilites = 0
    for i in range(len(Die_A)):
        for j in range(len(Die_B)):
            if int(Die_A[i]) + int(Die_B[j]) == 2: 
                print("dice combination ", Die_A[i], " , " , Die_B[j]," equal to the sum of 2")
                total_possibilites += 1
                
    print("And the probability of that happening is ", format(  total_possibilites/ (len(Die_A) * len(Die_B)), ".2%"))



def undoom_dice(Die_A, Die_B):
    New_Die_A = []
    New_Die_B = []
    
    for i in range(len(Die_A)):
        if Die_A[i] < 4:
            New_Die_A.append(Die_A[i]) 
        
    New_Die_B = [1]
    
    print("Dice A is 1,2,3, and Dice B can be 1 - infinity, so I just put 1 as a placeholder")    
    return New_Die_A, New_Die_B
    

if __name__ == "__main__":
   main()
