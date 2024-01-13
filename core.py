import random


debug = False
# if this is True, you can see the correct numbers in total,
# and the true password will be shown at the beginning

        
class LockBox:
    
    def __init__(self, figure: int) -> None:
        self.__figure = figure
        self.__passport = [random.randint(0, 9) for __ in range(self.__figure)]
    
    def match(self, pwd: list) -> list[bool | int]:
        res = []
        if len(pwd) == self.__figure:
            for i in range(self.__figure):
                if pwd[i] == self.__passport[i]:
                    res.append(True)
                elif pwd[i] in self.__passport:
                    res.append(0)
                else:
                    res.append(False)
        return res

    @property
    def passport(self): return self.__passport

class InteractManager:
    
    def __init__(self, figure: int, times: int) -> None:
        self.__figure = figure
        self.__times = times

    def output(self, msg) -> None:
        print("".join(['\n', msg, '\n']))
    
    def input(self) -> list[int]:
        while True:
            ipt = input(f"[{self.__figure}|{self.__times}]> ")
            try:
                if len(ipt) == self.__figure:
                    self.__times += -1
                    return [int(i) for i in ipt]
                else:
                    self.output(f"Length is {self.__figure}!")
            except ValueError:
                self.output("Your input is not numbers!")


def formatter(res: list[bool | int], ipt: list[int]) -> str:
    s = ""
    for i in range(len(res)):
        if res[i] is True:
            s = "".join([s, f"(\033[32m{ipt[i]}\033[0m)--"])
        elif res[i] is False:
            s = "".join([s, f"(\033[31m{ipt[i]}\033[0m)--"])
        else:
            s = "".join([s, f"(\033[33m{ipt[i]}\033[0m)--"])
    return s[:-2]

class Engine:
    
    def __init__(self, figure: int, times: int) -> None:
        self.__lockbox = LockBox(figure)
        self.__console = InteractManager(figure, times)
        self.__times = times

    def main(self) -> None:
        if debug:
            print(self.__lockbox.passport)
            
        for __ in range(self.__times):
            ipt = self.__console.input()
            res = self.__lockbox.match(ipt)
            
            s = formatter(res, ipt)
            self.__console.output(s)
            
            if all(res):
                self.__console.output("You win.")
                break
        else:
            self.__console.output("You lose.")
