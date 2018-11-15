"""Implement a class called Clock with the following attributes:

Constructor with three parameters: hours, minutes, seconds with default values 0.
Three instance variables: hours, minutes, seconds.
A method called str_update(). It takes as an argument a string of the form hh:mm:ss and updates
the three instances variables.
A __str__() method for responding to the print() method. It should write out: "{} hours, {} minutes and {} seconds"
A method called add_clocks(). It takes another clock object as a parameter, adds the two clocks and returns a new clock instance.  
In this method, you need to add the respective values of the two clocks together and remember the resulting hours, minutes and seconds. 
Remember that the sum of seconds cannot exceed 60, in which case there is a carry over to the minutes values. 
Same for minutes, it cannot exceed 60 and carries over to hours. For hours, the summed values cannot exceed
23. If hours is exceeded, we ignore it.  Use the divmod() built-in Python function in your implementation."""

class Clock:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    def str_update(self, string_clock):
        string_clock = string_clock.split(":")
        self.hours = int(string_clock[0])
        self.minutes = int(string_clock[1])
        self.seconds = int(string_clock[2])
    
    def add_clocks(self, time):
        seconds2 = divmod(self.seconds + time.seconds, 60)
        seconds_remain = seconds2[1]
        minutes_to_add = seconds2[0]
        minutes2 = divmod(self.minutes+ minutes_to_add + time.minutes, 60)
        minutes_remain = minutes2[1]
        hours_to_add = minutes2[0]
        hours2 = divmod(self.hours+ hours_to_add + time.hours, 24)
        hours_remain = hours2[1]
        return Clock(hours_remain, minutes_remain, seconds_remain)
        

    def __str__(self):
        return "{:d} hours, {:d} minutes and {:d} seconds".format(self.hours, self.minutes, self.seconds)

clock1 = Clock()
clock2 = Clock()
print(clock1)
print(clock2)
clock1.str_update("03:21:34")
clock2.str_update("05:45:52")
print(clock1)
print(clock2)
clock3 = clock1.add_clocks(clock2)
print(clock3)