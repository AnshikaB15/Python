
# Binary Search

class BinarySearch:

    def __init__(self):
        self.values = []

    def get_values(self):
        n = int(input("How many values you want to have in the collection: "))
        for i in range(0, n):
            self.values.append(int(input("Enter a value: ")))

    def print_values(self):
        print(f"\nValues in the Collection: {self.values}\n")

    def sort_values(self):
        self.values.sort()
        
    def binary_search(self, x):

        print(f"\nSearching for {x}...")
        
        start = 0
        end = len(self.values) - 1
        found = False

        while (not found) and (start <= end):
            mid = int((start + end) / 2)
            if x == self.values[mid]:
                found = True
                print(f"\tFound the value at index: {mid}")
                break
            elif x < self.values[mid]:
                end = mid - 1
            else:
                start = mid + 1

        if not found:
            print("\tValue was NOT found")

        print()
        
search = BinarySearch()
search.get_values()
search.sort_values()
search.print_values()

choice = 'Y'
while choice == 'Y':
    print()
    x = int(input("Enter the value that you want to search for: "))
    search.binary_search(x)
    choice = input("Do you want to try once again Y/N? ")

























