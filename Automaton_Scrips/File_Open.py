#----------------------------------------------------------------------------------------------------------------------------------------------
# -Every Things that storable it is treated as file (o/s terminogoly) 
# -File :- Unformated Uniform Stream of Bytes 
#         1). Unformated :- when we open any editor file are very Formatted but in case of Hard Disk it is not Formmatted (it is Unformated)
#         2). Uniform :- jr A la 1byte milat asl tr Small a la sudha 1byte ch milnar(inshort saglay na 1 bytech milnar)
#         3). Streams & Bytes  :- je ky store honar ahe te salag store honar ahe --------------- incase of bytes
#
# -File Opration Hai 2 Mood madhi Hotat :- 1)Text Mood
#                                          2)Binary Mood
#
# Open :- create & Open
#
#-----------------------------------------------------------------------------------------------------------------------------------------------


# q1 :- yes i can solve in which language (c,c++,java,python)
# q2 :- 



def main():

#-----------------------------------------------------------------------------------------------------------------------
# File Open krayechi ahe Demo.txt read krnay sathi "r"
#-----------------------------------------------------------------------------------------------------------------------
    open("Demo.txt","r")
    print("File gets Opened")

if __name__ == "__main__":
    main()