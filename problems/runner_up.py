# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.
# Input Format
# The first line contains . The second line contains an array   of  integers each separated by a space.
# Constraints


# Output Format
# Print the runner-up score.
# Sample Input 0
# 5
# 2 3 6 6 5
# Sample Output 0
# 5
# Explanation 0
# Given list is . The maximum score is , second maximum is . Hence, we print  as the runner-up score.


if __name__ == "__main__":
    number_of_digits = int(input())
    digits_in_str = input().strip().split()
    
    digits = list(map(int, digits_in_str))
    unique_diffs = list(dict.fromkeys(digits))
    second_largest = sorted(unique_diffs)[-2]
    print(second_largest)