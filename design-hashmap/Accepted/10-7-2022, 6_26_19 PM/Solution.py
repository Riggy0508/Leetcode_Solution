// https://leetcode.com/problems/design-hashmap

class MyHashMap:

    def __init__(self):
        self.my_dict = []
        self.key_list = []

    def put(self, key: int, value: int) -> None:
        if key in self.key_list:
            for i in self.my_dict:
                if i[0] == key:
                    i[1] = value
        else:
            self.key_list.append(key)
            self.my_dict.append([key,value])

    def get(self, key: int) -> int:
        for i in self.my_dict:
            if i[0] == key:
                return i[1]
        return -1 
    def remove(self, key: int) -> None:
        if key in self.key_list:
            self.key_list.remove(key)
        for i in range(len(self.my_dict)):
            if self.my_dict[i][0] == key:
                self.my_dict.pop(i)
                break 
        # print(self.key_list,self.my_dict)