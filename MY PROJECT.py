#Your task is to find the name of the student with maximum marks after updation in marks 
#after updation in marks and the jump in the student's rank ie, previous rank-curent rank
#you are given with three lists lists'names,mark's and update's where
#Names contains the names of the student 
#Marks contain the marks of the same student
#Updates contains the integers by which the marks of these studends are to be updated
#number of levels a student is ranking up or down must be displayed

#marks of the students before updation

marks = [('ram',[10,20,30]),('joe',[40,50,60]),('peter',[70,80,90])]

#updation in marks

marks[0][1][2]=35
marks[1][1][1]=45
marks[2][1][0]=75

#calculation of total marks

for i,j in marks:
    total=sum(j)
    print(i,total)

#calculation of maximum marks

l=[]
for i,j in marks:
    l.append(sum(j))

    maximum = max(l)
    for i,j in marks:
        if maximum == sum(j):
            print(i)



    # cLculation of rank

    l.sort(reverse=True)
    print(l)

    #finding the jump of the student

    for i,j in marks:
        if maximum == sum(j):
           a=l.index(maximum)
           print(a)


# previous rank
    b = a-1
    print(b)

 # current rank

    print(a)

