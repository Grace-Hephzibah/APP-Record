def hyphensepwords():
    items=[n for n in input().split('-')]
    items.sort()
    print('-'.join(items))
hyphensepwords()
