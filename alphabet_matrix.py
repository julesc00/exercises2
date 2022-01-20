
# Create matrix
alphabet = "ABCDEFGHIJKLMNOPQRSTUVXWYZ"
x_area = [ltr for ltr in alphabet[:N]]
y_area = [n for n in range(1, len(x_area) + 1)]
matrix = [[f"{str(y)}{str(x)}" for x in x_area] for y in y_area]
print(matrix)