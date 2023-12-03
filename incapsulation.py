class A:
    val1 = 1
    _val2 = 2 #protected
    __val3 = 3 #private

class B(A):
    pass


#val1 should be visible only in class A
b = B()
print(b.val1)
print(b._val2)