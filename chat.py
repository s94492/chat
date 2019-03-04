import os

def readfile(filname):
    lines = []
    with open (filname,'r',encoding='utf-8-sig') as i :
         for line in i :
             lines.append(line.strip())
    return lines

#def convert (lines):
   # for line in lines :
    #    if line == 'Allen'

def main ():
    lines= readfile('input.txt')
    print (lines)

main()
