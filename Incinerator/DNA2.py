golf=lambda s,p:''.join(sorted([s[i:i+p] for i in range(0,len(s)-p+1,p)],key=lambda a:sum([a[j]<a[i] for i in range(len(a)-1) for j in range(i+1,len(a))])))

