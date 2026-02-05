# link to problem: https://www.hackerrank.com/challenges/stat-warmup/problem?isFullScreen=true

# Input Format
# The first line contains the number of integers.
# The second line contains space separated integers for which you need to find the mean, median, mode, standard deviation and confidence interval boundaries.
# Constraints
# 10 <= N <= 2500
# 0 < xi <= 105
# Output Format
# A total of five lines are required.
# Mean (format:0.0) on the first line
# Median (format: 0.0) on the second line
# Mode(s) (Numerically smallest Integer in case of multiple integers)
# Standard Deviation (format:0.0) 
# Lower and Upper Boundary of Confidence Interval (format: 0.0) with a space between them.
# Sample Input
# 10
# 64630 11735 14216 99233 14470 4978 73429 38120 51135 67060
# Sample Output
# 43900.6
# 44627.5
# 4978
# 30466.9
# 25017.0 62784.2
# Note
# Use the constant 1.96 while computing the confidence interval.
# Scoring
# Scoring is proportional to the number of test cases cleared.



import sys
import numpy as num


def statistics(text):
    input = text.splitlines()
    numbers_count = map(int, input[0].strip().split())
    numbers = list(map(int, input[1].strip().split()))

    mean = num.mean(numbers)
    print(mean)
    
    
    print(num.median(numbers))

    counts = num.bincount(numbers)
    mode = num.argmax(counts)
    print(mode)

    deviation = num.std(numbers)
    print(f"{deviation:.1f}")

    n = len(numbers)
    sem = deviation / num.sqrt(n)

    lower_ci = (mean - 1.96 * sem)
    upper_ci = (mean + 1.96 * sem)
    print(f"{lower_ci:.1f} {upper_ci:.1f}")

if __name__ == '__main__':
    text = sys.stdin.read()
    statistics(text)