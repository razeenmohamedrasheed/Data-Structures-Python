lst = ['a','e','i','o','u','A','E','I','O','U']
        n = len(s)
        m, n = s[:n//2], s[n//2:]
        count, count1 = 0, 0
        for i in range(len(m)):
            if m[i] in lst:
                count += 1
            if n[i] in lst:
                count1 += 1
        return count == count1