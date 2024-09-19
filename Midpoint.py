'''
Ajay, Binoy and Chandru were very close friends at school. They were very good in Mathematics and they were the pet students of Emily Mam. Their gang was known as 3-idiots. Ajay, Binoy and Chandru live in the same locality. A new student Dinesh joins their class and he wanted to be friends with them. He asked Binoy about his house address. Binoy wanted to test Dinesh's mathematical skills. Binoy told Dinesh that his house is at the midpoint of the line joining Ajay's house and Chandru's house. Dinesh was puzzled. Can you help Dinesh out? Given the coordinates of the 2 end points of a line (x1,y1) and (x2,y2), write a python program to find the midpoint of the line. Input Format: Input consists of 4 integers. The first integer corresponds to x1 . The second integer corresponds to y1. The third and fouth integers correspond to x2 and y2 respectively. Output Format: Refer Sample Input and Output for exact formatting specifications. [All floating point values are displayed correct to 1 decimal place]
 
Input (stdin)
2
4
10
15
 
Output (stdout)
Binoy's house is located at (6.0,9.5)
'''
# Input the coordinates of the two points
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

# Calculate the midpoint
midpoint_x = (x1 + x2) / 2
midpoint_y = (y1 + y2) / 2

# Output the midpoint
print(f"Binoy's house is located at ({midpoint_x:.1f},{midpoint_y:.1f})")
