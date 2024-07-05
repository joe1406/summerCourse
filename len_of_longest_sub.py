# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
s = 'kwwebw'
def substring(str):
    sub_list = list(str)
    print(sub_list)
    the_list = []
    for i in range(0,len(str)):
        if sub_list[i] in the_list:
            return the_list
        else:
            the_list.append(sub_list[i])

print(substring(s))
