
# Linear Search

class LinearSearch:

    def __init__(self):
        self.values = []

    def get_values(self):
        n = int(input("How many values you want to have in the collection: "))
        for i in range(0, n):
            self.values.append(int(input("Enter a value: ")))

    def print_values(self):
        print(f"\nValues in the Collection: {self.values}\n")
        
    def linear_search(self, x):

        print(f"\nSearching for {x}...")
        
        position = -1
        found = False
        
        for value in self.values:
            position += 1
            if value == x:
                found = True
                print(f"\tFound the value at index: {position}")

        if not found:
            print(f"\tThe given value was not found in the collection")

        print()

search = LinearSearch()
search.get_values()
search.print_values()

choice = 'Y'
while choice == 'Y':
    print()
    x = int(input("Enter the value that you want to search for: "))
    search.linear_search(x)
    choice = input("Do you want to try once again Y/N? ")































