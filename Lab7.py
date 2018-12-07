##################################################################
#Author- Nusrat Sarmin
#Date-12/05/2018
#This method will calculate the edit distance between two words.
#Will also display the matrix of comparison between two strings.
##################################################################

def edit_distance(s1, s2, l1, l2):
    d = [[0 for x in range(l2 + 1)] for x in range(l1 + 1)]

    for i in range(l1+1):
        for j in range(l2+1):
            if i == 0:
                d[i][j] = j
            elif j == 0:
                d[i][j] = i
            elif s1[i-1] == s2[j-1]:
                d[i][j] = d[i-1][j-1]

            else:
                d[i][j] = 1 + min(d[i][j-1], d[i-1][j],d[i-1][j-1])
    return d[l1][l2]


s1 = "Stack"
s2 = "Stock"

print ("The two strings are " + s1 + " and " + s2)
print("Edit Distance of " + s1 + " and " + s2 + " is : " + str(edit_distance(s1, s2, len(s1), len(s2))))
