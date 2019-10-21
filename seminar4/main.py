import getopt, sys, time

def print_perms(elements):
    print("\tCombinations\n")
    for perm in perms:
        for element in perm:
            print("\t" + str(element),end = " ")
        print("")
    print("\n\tThere are " + str(len(elements)) + " combinations.\n")

def permutations(elements, accum = []):
    if len(elements) == 1:
        return [accum + elements]
    perms = []
    for element in elements:
        new_elements = list(elements)
        new_elements.remove(element)
        perms += permutations(new_elements, accum + [element])
    return perms

def generate_elements(number_of_elements):
    return [i for i in range(0, number_of_elements)]

number_of_elements = int(getopt.getopt(sys.argv[1:], "")[1][0])
elements = generate_elements(number_of_elements)
start = time.time()
perms = permutations(elements)
end = time.time()
print_perms(perms)
print("\tElapsed time was: " + str(end - start) + " seconds")