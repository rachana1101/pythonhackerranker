# There is an array of  integers. There are also  disjoint sets,  and , each containing  integers. You like all the integers in set  and dislike all the integers in set . Your initial happiness is . For each integer in the array, if , you add  to your happiness. If , you add  to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.
# Note: Since  and  are sets, they have no repeated elements. However, the array might contain duplicate elements.
# Constraints



# Input Format
# The first line contains integers  and  separated by a space.
# The second line contains  integers, the elements of the array.
# The third and fourth lines contain  integers,  and , respectively.
# Output Format
# Output a single integer, your total happiness.
# Sample Input
# 3 2
# 1 5 3
# 3 1
# 5 7
# Sample Output
# 1
# Explanation
# You gain  unit of happiness for elements  and  in set . You lose  unit for  in set . The element  in set  does not exist in the array so it is not included in the calculation.
# Hence, the total happiness is .

import sys

def like_dislike(text): 
    data = text.splitlines()
    n1, n2 = map(int, data[0].strip().split())  # 5 5 → [5, 5]
    my_numbers = list(map(int, data[1].strip().split()))  # [1,2,3,4,5]
    like_list = list(map(int, data[2].strip().split()))   # [1,3,5,7,9]  
    unlike_list = list(map(int, data[3].strip().split())) # [2,4,6,8,10]

    like_list_set = set(like_list)
    unlike_list_set = set(unlike_list)

    score = 0
    # if (len(my_numbers)) != n1: 
    #     score = 0
    # if (len(data) != 4):
    #     score = 0
    # if (len(like_list) != n2 and len(unlike_list) != n2):
    #     score = 0     

    for my_num in my_numbers: 
        if my_num in like_list_set:
            score = score + 1
       
    for my_num in my_numbers: 
        if my_num in unlike_list_set:
            score = score -1             

    print(score)

if __name__ == '__main__':
    text = sys.stdin.read()
    like_dislike(text)
    
