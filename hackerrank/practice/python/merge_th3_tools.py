##pretty easy
def merge_the_tools(string, k):
    subs = [string[i:i+k] for i in range(0,len(string),k)] #splits at every nth char
    for elm in subs:
        print(''.join(dict().fromkeys(elm).keys())) #dict only has "unique" keys

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
