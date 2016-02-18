##############################It finds all the correct subsequences in a given sequence#######################
from __future__ import generators

def KnuthMorrisPratt(text, pattern):

    '''Yields all starting positions of copies of the pattern in the text.
Calling conventions are similar to string.find, but its arguments can be
lists or iterators, not just strings, it returns all matches, not just
the first one, and it does not need the whole text in memory at once.
Whenever it yields, it will have read the text exactly up to and including
the match that caused the yield.'''

    # allow indexing into pattern and protect against change during yield
    pattern = list(pattern)

    # build table of shift amounts
    shifts = [1] * (len(pattern) + 1)
    shift = 1
    for pos in range(len(pattern)):
        while shift <= pos and pattern[pos] != pattern[pos-shift]:
            shift += shifts[pos-shift]
        shifts[pos+1] = shift

    # do the actual search
    startPos = 0
    matchLen = 0
    for c in text:
        while matchLen == len(pattern) or \
              matchLen >= 0 and pattern[matchLen] != c:
            startPos += shifts[matchLen]
            matchLen -= shifts[matchLen]
        matchLen += 1
        if matchLen == len(pattern):
            yield startPos
###################################################################################################
import csv

min_support = 0.04
total_student_number = 1412

#all transactions list
csvfile=open('data-2016.csv', 'rb')
reader1=csv.reader(csvfile, delimiter=';', quotechar='"')
courses_transaction = []
one_transaction = []
for row in reader1:
    for i in range(2, len(row), 5):
        code=row[i]
        one_transaction.append(int(code))
    courses_transaction.append(one_transaction)
    one_transaction = []
#print courses_transaction

#count support for one course
def count_support_one(code):
    csvfile=open('data-2016.csv', 'rb')
    csv_reader= csv.reader(csvfile, delimiter=';', quotechar='"')
    student_count_courses = 0
    total_student_count=0
    for row in csv_reader:  #iterate over rows
        total_student_count+=1 #calculate the number of students (rows)
        for i in range(2, len(row), 5):
            if(row[i]==code):   #if we found coursecode we were looking for, increase the support count
                student_count_courses+=1
                break       #and don't look for more courses
    return (student_count_courses*1.0/total_student_count*1.0)  #then coutn the support

def make_list(e):
    e = [e]
    return e

def find_minsup_courses():
    csvfile=open('data-2016.csv', 'rb')
    reader=csv.reader(csvfile, delimiter=';', quotechar='"')
    courses_counted_succ=set()
    courses_counted_fail=set()
    for row in reader:
        for i in range(2, len(row), 5):
            code=row[i]
            if(code in courses_counted_fail): #If already failed, don't count again
                continue
            if(code not in courses_counted_succ): #If we already know that support > 0.04 don't calculate it again
                supp=count_support_one(code)
                if(supp < min_support):
                    courses_counted_fail.add(code)
                    continue
            courses_counted_succ.add(code) #Add to success set
    temp = map(int, courses_counted_succ)
    courses_counted = map(make_list, temp)
    return courses_counted

f1 = find_minsup_courses() #find 1 frequent itemset

def count_support(itemset, transactions):
    count_number = 0
    for one_student in transactions:
            for s in KnuthMorrisPratt(one_student, itemset):
                if(s>0):
                    count_number+=1
    return round(float(count_number)/float(total_student_number),4)

#print count_support([582514], courses_transaction)

def apriori_gen(keys1):
    keys2 = []
    for k1 in keys1:
        for k2 in keys1:
            if k1 != k2:
                key = []
                for k in k1:
                    if k not in key:
                        key.append(k)
                for k in k2:
                    if k not in key:
                        key.append(k)
                key.sort()
                if key not in keys2:
                    keys2.append(key)
            
    return keys2

def candidate_gen_prune(itemsets):
    c = 0
    k_plus1_set = apriori_gen(itemsets)
    new_set = []
    while(1):
        print "haha"
        for i in k_plus1_set:
            if(count_support(i, courses_transaction)>min_support):
                new_set.append(i)
                k_plus1_set.remove(i)
                c += 1
                print len(k_plus1_set)
        if (len(k_plus1_set) == 0):
            return new_set
        else:    
            k_plus1_set = new_set
            new_set = []
        k_plus1_set = apriori_gen(k_plus1_set)

print candidate_gen_prune(f1)


