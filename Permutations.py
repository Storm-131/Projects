# Permutations

if __name__ == '__main__':
    x = 1
    y = 1
    z = 2
    n = 3

x_l = list(range(0, x+1))
y_l = list(range(0, y+1))
z_l = list(range(0, z+1))

# using list comprehension
# to compute all possible permutations
res = [[x, y, z] for x in x_l
                 for y in y_l
                 for z in z_l if (x+y+z !=n)]

# printing result
print("All possible permutations are : " + str(res))
