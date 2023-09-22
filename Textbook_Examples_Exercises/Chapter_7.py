# Importing the circle.py file from the Resources folder
import sys
sys.path.append(r'C:\Users\devil\OneDrive\Desktop\MIT Courses\6.0001A - Introduction_To_Computer_Science_And_Programming_In_Python\Textbook_Examples_Exercises\Resources')
import circle

# Using the functions in circle.py
pi = 3 # not the same pi as in the circle.py file
print(pi) 
print(circle.pi) # pi from the circle.py file
print(circle.area(3))
print(circle.circumference(3))
print(circle.sphere_surface(3))


# Importing the calendar module and displaying March 1949
import calendar as cal
cal_english = cal.TextCalendar()
print(cal_english.formatmonth(1949, 3))

# Displaying March 1949 in different languages
fr_cal = cal.LocaleTextCalendar(locale = 'fr_FR').formatmonth(1949, 3)
pl_cal = cal.LocaleTextCalendar(locale = 'pl_PL').formatmonth(1949, 3)
da_cal = cal.LocaleTextCalendar(locale = 'da_dk').formatmonth(1949, 3)

print(fr_cal)
print(pl_cal) 
print(da_cal)

# Determining what day Christmas will fall on in 2033
print(cal.day_name[cal.weekday(2033, 12, 25)])
