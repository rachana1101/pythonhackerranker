#!/bin/python3

# When users post an update on social media,such as a URL, image, status update etc., other users in their network are able to view this new post on their news feed. Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.
# Since sometimes posts are published and viewed in different time zones, this can be confusing. You are given two timestamps of one such post that a user can see on his newsfeed in the following format:
# Day dd Mon yyyy hh:mm:ss +xxxx
# Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.
# Input Format
# The first line contains , the number of testcases.
# Each testcase contains  lines, representing time  and time .
# Constraints
# Input contains only valid timestamps
# .
# Output Format
# Print the absolute difference  in seconds.
# Sample Input 0
# 2
# Sun 10 May 2015 13:54:36 -0700
# Sun 10 May 2015 13:54:36 -0000
# Sat 02 May 2015 19:54:36 +0530
# Fri 01 May 2015 13:54:36 -0000
# Sample Output 0
# 25200
# 88200
# Explanation 0
# In the first query, when we compare the time in UTC for both the time stamps, we see a difference of 7 hours. which is  seconds or  seconds.
# Similarly, in the second query, time difference is 5 hours and 30 minutes for time zone adjusting for that we have a difference of 1 day and 30 minutes. Or

import os
from datetime import datetime, timezone

# Complete the time_delta function below.
def time_delta(date1, date2):
    date_1 = datetime.strptime(date1, "%a %d %b %Y %H:%M:%S %z")
    date_2 = datetime.strptime(date2, "%a %d %b %Y %H:%M:%S %z")
    return(int((date_1.astimezone(timezone.utc) - date_2.astimezone(timezone.utc)).total_seconds()))

if __name__ == '__main__':
    num_of_input = int(input())

    result = []
    for _ in range(num_of_input): 
        t1 = input()
        t2 = input()
        result.append(time_delta(t1, t2))

    for i in range(len(result)): 
        print(abs(result[i]))
