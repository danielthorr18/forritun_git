def input_vector(size):
    return_vector = []
    for i in range(0, size):
        return_vector.append(float(input(("Element no {}: ".format(i+1)))))
    
    return return_vector

def dot_product(vec1, vec2):
    new_vec = []
    for i in range(len(vec1)):
        new_vec.append(vec1[i] * vec2[i])

    return (sum(new_vec))
# Main program starts here, DO NOT change
size = int(input("Input vector size: "))
vector1 = input_vector(size)
vector2 = input_vector(size)
print("Dot product is:", dot_product(vector1, vector2))