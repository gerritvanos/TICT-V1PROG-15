#A
s = '10 20 30 40 50 60'
lst= s.split()
print(lst)
#B
s = '10,20,30,40,50,60'
lst = s.split(',')
print(lst)
#C
s = '10&20&30&40&50&60'
lst = s.split('&')
print(lst)
#D
s = '10 - 20 - 30 - 40 - 50 - 60'
lst = s.split(' - ')
print(lst)