"""

"""









heli = Card_holder(101, "Heli", "Toronto")
niti = Card_holder(103, "Niti", "Toronto")
anshika = Card_holder(105, "Anshika", "Phoenix")

potter = Book("B-101", "Harry Potter", "Rowling")
jackson = Book("B-102", "Percy Jackson", "Riordan")

potter.checkout_by(heli)
potter.checkout_by(anshika)

jackson.checkout_by(niti)
jackson.checkout_by(heli)

# This should print all book details of 'jackson' object, and also the list of card holders who are reading this book now
print(jackson)

# This should print all details of 'heli' object, and list of all books that 'heli' has checked out.
# This one may need extra stuff to be taken care. So, optional.
print(heli)

# Make changes to the above flow, as per your requirements.

