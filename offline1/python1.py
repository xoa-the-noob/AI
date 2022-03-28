tuplelist1 = [
                    ('parent','Hasib','Rakib'),
                    ('parent','Rakib','Sohel'),
                    ('parent','Rakib','Rebeka'),
                    ('parent','Rashid','Hasib'),
                    ('parent','Sohel','Ann'),
                    ('parent','Rebeka','Sam')
                    
            
              ]
tuplelist2 = [
                    ('male','Hasib'),
                    ('male','Sohel'),
                    ('male','Rakib'),
                    ('male','Rashid'),
                    ('male','Sam'),
                    ('female','Ann'),
                    ('female','Rebeka'),
              ]

X1=str(input("Sibling name for finding brother:"))
print('Brother:')
i1,j1,k1=0,0,0
while(i1<=5):
    if((tuplelist1[i1][0] == 'parent')&(tuplelist1[i1][2] == X1)):
        for j1 in range(6):
            if( (tuplelist1[j1][0] == 'parent') & ((tuplelist1[i1][1] == tuplelist1[j1][1]) & (tuplelist1[j1][2]!=X1))):
                for k1 in range(7):
                    if((tuplelist2[k1][1] == tuplelist1[j1][2]) & (tuplelist2[k1][0] == 'male')):
                        print(tuplelist1[j1][2]," ")

    i1 = i1 + 1

X2=str(input("Sibling name for finding sister:"))
print('Sister:')

i2,j2,k2=0,0,0
while(i2<=5):
    if((tuplelist1[i2][0] == 'parent')&(tuplelist1[i2][2] == X2)):
        for j2 in range(6):
            if( (tuplelist1[j2][0] == 'parent') & ((tuplelist1[i2][1] == tuplelist1[j2][1]) & (tuplelist1[j2][2]!=X2))):
                for k2 in range(7):
                    if((tuplelist2[k2][1] == tuplelist1[j2][2]) & (tuplelist2[k2][0] == 'female')):
                        print(tuplelist1[j2][2]," ")

    i2 = i2 + 1



X3=str(input("Neice/Nephew name for finding uncle:"))
print('Uncle:')
m,n=0,0

while(m<=5):
    if((tuplelist1[m][0] == 'parent')&(tuplelist1[m][2] == X3)):
        for n in range(6):
            if( (tuplelist1[n][0] == 'parent') & (tuplelist1[m][1] == tuplelist1[n][2]) ):
                i3,j3,k3=0,0,0
                while(i3<=5):
                   if((tuplelist1[i3][0] == 'parent')&(tuplelist1[i3][2] == tuplelist1[n][2])):
                     for j3 in range(6):
                       if( (tuplelist1[j3][0] == 'parent') & ((tuplelist1[i3][1] == tuplelist1[j3][1]) & (tuplelist1[j3][2]!=tuplelist1[n][2]))):
                           for k3 in range(7):
                              if((tuplelist2[k3][1] == tuplelist1[j3][2]) & (tuplelist2[k3][0] == 'male')):
                                    print(tuplelist1[j3][2]," ")

                   i3 = i3 + 1
    m = m + 1

X4=str(input("Neice/Nephew name for finding aunt:"))
print('Aunt:')
q,r=0,0

while(q<=5):
    if((tuplelist1[q][0] == 'parent')&(tuplelist1[q][2] == X4)):
        for r in range(6):
            if( (tuplelist1[r][0] == 'parent') & (tuplelist1[q][1] == tuplelist1[r][2]) ):
                i4,j4,k4=0,0,0
                while(i4<=5):
                   if((tuplelist1[i4][0] == 'parent')&(tuplelist1[i4][2] == tuplelist1[r][2])):
                     for j4 in range(6):
                       if( (tuplelist1[j4][0] == 'parent') & ((tuplelist1[i4][1] == tuplelist1[j4][1]) & (tuplelist1[j4][2]!=tuplelist1[r][2]))):
                           for k4 in range(7):
                              if((tuplelist2[k4][1] == tuplelist1[j4][2]) & (tuplelist2[k4][0] == 'female')):
                                    print(tuplelist1[j4][2]," ")

                   i4 = i4 + 1    
    q = q + 1





