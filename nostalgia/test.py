

with open('song_hashes.txt','r') as file:
    song_name  , count = file.readline().split(' ')
    current_char = file.readline()
    current_count = file.readline()
    print(song_name)
    print(count)
    current_char =[ x for x in current_char.split()]
    current_count = [int(x) for x in current_count.split()]
    print(current_char[0])
    print(current_char[1])
    print(current_char[2])
    print(current_char[3])
    print(current_count[0] + 7)
    print(current_count[1])
    print(current_count[2])
    print(current_count[3])


