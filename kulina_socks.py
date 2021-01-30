#!/usr/bin/env python
# coding: utf-8

# In[10]:


loopflag = True
while loopflag:
    countsock = int(input('Input jumlah kaos kaki : '))
    socklist = input('Input warna kaos kaki : ')
    socklist = socklist.split(' ')
    sortedlist = sorted(socklist)

    if countsock != len(sortedlist):
        print('Jumlah kaos kaki tidak sesuai dengan jumlah warna yang diinput! \n')
    else:
        countpair = 0
        for ii in range(len(sortedlist)):
            if ii+1 ==  len(sortedlist):
                break
            else:
                if sortedlist[ii] == sortedlist[ii+1]:
                    sortedlist[ii] = 'paired'
                    sortedlist[ii+1] = 'paired'
                    countpair = countpair + 1
                else:
                    continue
        loopflag = False
        print('Jumlah pasang kaos kaki : ' + str(countpair))

