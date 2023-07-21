# def palstring(my_string): # Time complexity is lower
#     j=int(len(my_string))
#     for i in range(0,j//2):
#         if my_string[i] != my_string[len(my_string)-i-1]:  # Only checking is happenning
#             print(f"{my_string} is not palindrome")
#             break
#     else:
#         print(f"{my_string} is palindrome")

# palstring(input("String:"))
# def palstring(my_string): # Time Complexity is higher
#     listify_str = list(my_string)
#     for i in range(len(my_string)//2):
#         listify_str[i], listify_str[len(
#             my_string)-1-i] = listify_str[len(my_string)-1-i], listify_str[i]  # The reverse operation is actually happenning
#     if "".join(listify_str)==my_string:
#         print(f"\n\t\t{my_string} is palindrome")
#     else:
#         print(f"\n\t\t{my_string} is NOT palindrome")
# palstring(input("\n\t\tString:"))

# string=input("String:")
# print(string[::-1]) # Reverse READING done by Slicing
# print(string)