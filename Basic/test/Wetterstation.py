# Wetterstation 
temp = [12, 14 ,9, 12, 14, 16, 15, 15, 9, 8, 13 ,13, 15, 12]
print(f"{min(temp)} is the lowes temperature on {temp.index(min(temp)) + 1} day")
print(f"{max(temp)} heigest temparature on {temp.index(max(temp)) + 1} day")
max_div: int = 0
max_day: int = 0
min_day: int = 0
for i in range(len(temp) - 1):
    if max_div > abs(temp[i] - temp[i + 1]):
        min_day = i+1
        max_day =i +2





