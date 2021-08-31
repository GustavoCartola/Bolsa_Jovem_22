N = int(input())

doisadois = (N*(N-1)) / 2

quatroaquatro = (N*(N-1)*(N-2)*(N-3)) / 24

final = quatroaquatro + doisadois + 1

print(int(final))