#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# Prediction:
# # output > 5
# Correct


#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# Prediction:
# # output > Error, expected 2 arguments, got 0
# Correct if first function is included
# Wrong if function isn't included: function not defined


#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# Prediction:
# # output > 5
# Correct

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# Prediction:
# # output > 5
# Actual: 

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# Prediction:
# # output > 5
# # output > None
# Correct


#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
# Prediction:
# # output > 3
# # output > 5
# # output > Error, cannot add None + None
# Correct (TypeError)


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# Prediction:
# # output > "25"
# Correct


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# Prediction:
# # output > 100
# # output > 10
# Correct


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# Prediction:
# # output > 7
# # output > 14
# # output > 21
# Correct


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# Prediction: 
# # output > 8
# Correct


#11
b = 500
print(b) # 1
def foobar():
    b = 300
    print(b)
print(b) # 2
foobar() # 3
print(b) # 4
# Prediction: 
# # output > 500
# # output > 500
# # output > 300
# # output > 500
# Correct


#12
b = 500
print(b) # 1
def foobar():
    b = 300
    print(b)
    return b
print(b) # 2
foobar() # 3
print(b) # 4
# Prediction: 
# # output > 500
# # output > 500
# # output > 300
# # output > 500
# Correct


#13
b = 500
print(b) # 1
def foobar():
    b = 300
    print(b)
    return b
print(b) # 2
b=foobar() # 3
print(b) # 4
# Prediction: 
# # output > 500
# # output > 500
# # output > 300
# # output > 300
# Correct


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# Prediction: 
# # output > 1
# # output > 3
# # output > 2
# Correct


#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
# Prediction:
# # output > 1
# # output > 3
# # output > 5
# # output > 10
# Correct