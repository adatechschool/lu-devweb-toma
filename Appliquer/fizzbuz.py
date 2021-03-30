class FizzBuzz:
    def __init__(self):
        pass
    def test(self, n: int, stage: int) -> str:
        if type(n) != int or type(stage) != int: return "'n' and 'stage' should be of type int"
        else: return self._fizzbuzz(n,stage)
    def _fizzbuzz(self, n: int, stage: int) -> str:
        string = ""
        if not n%3: string+="Fizz"
        if not n%5: string+="Buzz"
        if n%5 and n%3:
            if stage == 2:
                if '3' in str(n): string+="Fizz"
                if '5' in str(n): string+="Buzz"
            string = str(n)
        
        return string

fb = FizzBuzz()

for i in range(1,101):
    print(fb.test(i, 2))