def solve(N):
    if N == 0:
        return '0'
    if N == 1:
        return '1'

    if N % 2 == 0:
        return '0'+solve(N//-2)
    if N % 2 ==1:
        return '1'+solve((N-1)//-2)

print(solve(int(input()))[::-1])
