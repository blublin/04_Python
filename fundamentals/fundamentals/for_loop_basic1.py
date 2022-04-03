# Basic
print("Start Basic Loop")
for x in range(151):
	print(x)
print("End Basic Loop\n\n")

print("Start Multiples of 5 Loops")
# Multiples of 5
for x in range(5,1000,5):
	print(x)
print("End Multiples of 5 Loops\n\n")

print("Start Counting, the Dojo Way")
# Counting, the Dojo Way
for x in range(1,100):
	if not x % 10:
		print("Coding Dojo")
	elif not x % 5:
		print("Coding")
	else:
		print(x)
print("End Counting, the Dojo Way\n\n")

print("Start Woah. That Sucker's Huge")
# Woah. That Sucker's Huge
sum = 0
for x in range (1, 500000, 2):
	sum += x
print(f"Sum of odd numbers, 1 through 500k: {sum:,}")
print("End Woah. That Sucker's Huge\n\n")

print("Start Countdown by Fours")
# Countdown by Fours
count = 2018
while count > 0:
	print(count)
	count -= 4
print("End Conutdown by Fours\n\n")

print("Start Flexible Counter")
# Flexible Counter
lowNum, highNum, mult = 2, 1000, 17
while lowNum <= highNum:
	if not lowNum % mult:
		print(lowNum)
	lowNum += 1
print("End Flexible Counter")