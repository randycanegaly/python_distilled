import time

class Date:
    datefmt = '{year}-{month:02d}-{day:02d}'
    def __init__(self, year, month, day):#instance method
        self.year = year
        self.month = month
        self.day = day

    def __str__(self) -> str:# instance method
        return self.datefmt.format(year=self.year,
                                   month=self.month,
                                   day=self.day)
    
    @classmethod
    def from_timestamp(cls, ts):# class method
        tm = time.localtime(ts)
        return cls(tm.tm_year, tm.tm_mon, tm.tm_mday)
    
    @classmethod
    def today(cls): #class method
        return cls.from_timestamp(time.time())
    
#create an instance
a = Date(1958, 10, 23)
print(a)

#stamp = time.time()
#print(stamp)

#call each class method "properly"
ts_date = Date.from_timestamp(time.time())
print('ts_date', ts_date)

todate = Date.today()
print('todate', todate)

#call each class method "dirty"
print('dirty ...', a.from_timestamp(time.time()))
print('and .....', a.today())

class MDYDate(Date):#use inheritance to vary the format via the datefmt class variable
    datefmt = '{month}/{day}/{year}' #change the date format with a new format string

b = MDYDate(1984, 8, 17)
print('MDY', b)

    
