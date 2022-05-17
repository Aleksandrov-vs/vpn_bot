# a = A()
#
#
# class A(metaclass=MyMetaClass):
#     pass
#
#     def __init__(self):
#         print('init')
#
#     def __call__(self, *args, **kwargs):
#         print('call')
#         return super(A, self).__call__(self, *args, **kwargs)
#
#
# # class LittleMeta(type):
# #     def __new__(cls, clsname, superclasses, attributedict):
# #         print("clsname: ", clsname)
# #         print("superclasses: ", superclasses)
# #         print("attributedict: ", attributedict)
# #         return type.__new__(cls, clsname, superclasses, attributedict)
#
#
# class MyMetaClass(type):
#     def __new__(mcs, class_name, parents, attributes):
#         print('meta new')
#         return super().__new__(mcs, class_name, parents, attributes)
#
#     def __call__(self, *args, **kwargs):
#         print('meta call')
#         return type.__call__(self, *args, **kwargs)
#

import functools


def my_decorator(my_funk):
    # @functools.wraps(wrapped=)
    def wrapper(*args, **kwargs):
        print('my_decor')
        for i in args:
            print(i)
        return my_funk(*args, **kwargs)
    return wrapper


@my_decorator
def main(a, b, c):
    print("main")

if __name__ == "__main__":
    main(1, 2, 3)
