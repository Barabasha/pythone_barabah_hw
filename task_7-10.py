print ('======================Task7======================')
usa_date = '04.08.2017'
europe_date = usa_date[3:6] + usa_date[:3] + usa_date [6:]
print ('usa_date    ', usa_date)
print ('europe_date ', europe_date)
print()

print ('======================Task8======================')
s1 = 'xxxx'
s2 = '0000'
print (s1)
print (s2)
abrakadabra_s1 = s2[:int(len(s2)/2)] + s1 + s2[int(len(s2)/2):]
print (abrakadabra_s1)
abrakadabra_s2 = s1[:int(len(s1)/2)] + abrakadabra_s1 + s1[int(len(s1)/2):]
print (abrakadabra_s2)
print()

print ('======================Task9======================')
s1 = 'we study phyton3'
idx1 = s1.find(' ')
idx2 = idx1 + s1[idx1+1:].find(' ') + 1
s2 = s1[idx1+1:idx2]
result = s1[:idx1+1] + s2.upper() + s1[idx2:]
print(result)
print()

print ('======================Task10=====================')
s = 'Leo Tolstoy*1828-08-28*1910-11-20'
idx1 = s.find ('*') #find the beginning of the year of birth
idx11 = s.find ('-') #find the end of the year of birth
birth = s[idx1+1 : idx11]
idx2 = s[idx1+1:].find('*') + idx1 +2  #find the beginning of the year of death
idx21 = s[idx2:].find('-') + idx2   #find the end of the year of death
death = s[idx2 : idx21]
name = '"' + s[:idx1] + '",'
years = int(death) - int(birth)
print (name, years)
