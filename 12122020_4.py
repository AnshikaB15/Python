"""
    Example of Method Overriding.

    Method overriding is a form of Polymorphism.
    Method overriding is the concept of a Child class overriding the
        behavior of Parent Class.

    Both Parent and Child classes should have method with the same name,
      and same parameters.

    When we invoke the method on Child object, it will override what's in
      the parent.
"""

class GrandParent:
    def show(self):
        print("In show() of GrandParent")

    def display(self):
        print("In display() of GrandParent")

class Parent(GrandParent):
    def display(self):
        print("In display() of Parent")
    
    def explain(self):
        print("In explain() of Parent")

class Child(Parent):
    def explain(self):
        print("In explain() of Child")

    def demo(self):
        print("In demo() of Child")

child = Child()
child.demo()
child.explain()
child.display()
child.show()

parent = Parent()
# parent.demo()
parent.explain()
parent.display()
parent.show()



