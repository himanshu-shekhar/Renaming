import sys,os

##Just change the next line
myName="Rogue"

for i in range(1,len(sys.argv)+1):
    fname=sys.argv[i]
    index=sys.argv[i].rfind('.')
    os.rename(fname,fname[:index]+myName+fname[index:])


##In windows open run (by pressing win+R key)
##Then type "shell:sendto" and press enter
##Copy this file in that folder (sendTo folder)
##Now select the files which you have to rename
##Right click -> sendTo -> rename
##And you are done :)
