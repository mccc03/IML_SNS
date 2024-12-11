def convdim(N,F,P,S):
    return (N-F+2*P)/S + 1
def pooldim(w,h,F,S):
    return [(w-F)/S +1,(h-F)/S +1]

N = 21      # 'Image' size
F = 3       # Kernel (filter - F) size
P = 0       # Padding
S = 2       # Stride

print(convdim(N,F,P,S))
print(pooldim(N,N,F,S))