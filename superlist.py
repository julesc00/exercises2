
class SuperList(list):
    def __len__(self):
        return 1000


super_list1 = SuperList()

print(super_list1.__len__())
super_list1.append(5)
print(super_list1[0])
print(issubclass(SuperList, list))
