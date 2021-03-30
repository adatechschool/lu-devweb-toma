class Leap :
    def __init__(self):
        pass
    def test(self, year: int) -> bool:
        if type(year) != int or year < 1583: return "Error: Invalid year"
        else: return self._is_leap(year)
    def _is_leap(self, year: int) -> bool:
        if year%4: return False
        elif not year%400: return True
        elif year%100: return True
        else: return False

l = Leap()
for y in [2000,2003,1900,1700,1600,1884, "coucou", 1582]:
    print(l.test(y))