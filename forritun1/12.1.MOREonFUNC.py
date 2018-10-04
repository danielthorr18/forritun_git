def music_func(kind = "Classic Rock", group = "The Beatles", vocal = "Freddie Mercury"):
    print("The best kind of music is {}".format(kind))
    print("The best music group is {}".format(group))
    print("The best lead vocalist is {}".format(vocal))

    
    #definition for music_func goes here

def main():
    music, group, singer = input("Input music, group, singer: ").split(',')
    music_func(music, group, singer)
    music_func()

main()