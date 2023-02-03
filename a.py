import io
import sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
#str = input()
#print(str)
# print('hello world!')
def check_1(clist):
    while '()' in clist or '[]' in clist or '\{\}' in clist:
        clist = clist.replace('()','')
        clist = clist.replace('[]','')
        clist = clist.replace('\{\}','')
    return clist == ''

if __name__ == '__main__':
    demo = "\{(((({}))))[()]\}()"
    print(check_1(demo))