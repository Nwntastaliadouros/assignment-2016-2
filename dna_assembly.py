def addnewedgeandnode(n,edge):
    if len(lakm)==0:
        return
    n=n+1
    #print()
    #print("first=",seq[n-1])
    #print("seq so far ...=",seq)
    #print("Depth of recursive n=",n)
    #print("legth of remaining edges before a11 ",len(lakm))
    a=len(lakm)
    aedge=edge
    for a11 in lkom:
        if len(lakm)==0:
            return
        if (a11[0:k-2]==lca[n-1]):
            ## find edge and remove it from list
            #print("Depth= ",n,"a11=",a11)
            #print(seq[n-1])
            #print(a11[k-2:k-1])
            edge=seq[n-1]+a11[k-2:k-1]
            #print("edge is ",edge)
            if edge in lakm:
                lakm.remove(edge)
                seq.append(a11)
                #print("sequence so far inside recursive ",seq)
                #print("edges remaining ..",lakm)
                if (len(lakm)==0):
                    #print("The path has created")
                    break
                else:
                    lca.append(a11[1:k-1])
                    #print("lca inside ",lca)
                    first=a11
                    addnewedgeandnode(n,edge)
            #else:
                #print("edge not found",edge)
    if a==len(lakm):
        #print("Edge not added you must pop or add ================================")
        seq.pop()
        #print(seq)
        lakm.append(aedge)
        #print(lakm)
        lca.pop()
    #######################
    return
###############################################
import sys
ff=sys.argv[1]

lkom=[]     ## Λίστα που περιέχει τους κόμβους
lakm=[]     ## Λίστα που περιέχει τις ακμές
##############################################
## Find the number k
f = open(ff, 'r')
word=f.readline()
k=len(word)-1
#print(k)
f.close()
##############################################
f = open(ff, 'r')
for line in f.readlines():
    words=line.split()
    for word in words:
        if word not in lakm:
            lakm.append(word)
        lw=word[0:k-1]
        rw=word[1:k]
        if lw not in lkom:
            lkom.append(lw)
        if rw not in lkom:
            lkom.append(rw)
#        print(word)
#print("List of unique nodes ",lkom)
#print("List of unique edges ",lakm)
## Now lkom holds unique nodes
## Now lakm holds unique edges
###############################################
non=len(lkom)   ## Number of nodes
noe=len(lakm)
#print("Number of nodes ",non)
#print("Number of edges ",noe)
seq=[]      ## Λίστα ακολουθίας
###############################################
lca=[]
#################################
n=0     ## Shows the depth of recursive
first=lkom[0]   ## First node
seq.append(first)
#print("Sequence so far  ... ",seq)
#print("First node =",first)
#print(seq[0])
## find the last if k=3 and the 2 last if k=4
#print(lkom[0][1:k-1])
lca.append(lkom[0][1:k-1])    ## Add the second letter of node in List lca
#print("List lca so far ...",lca)
#print("recursive begins ... ")
edge=""
addnewedgeandnode(n,edge)

#print(seq)
#print(len(seq))

chain=""
nn=0
for xx in seq:
    nn=nn+1
    if nn==1:
        chain=xx
    elif (nn<len(seq)-1):
        chain=chain+xx[k-2:k-1]
    print(chain)    
################################
