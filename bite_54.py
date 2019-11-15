INDENTS = 4


def print_hanging_indents(poem):
    poem_listed = poem.split('\n')
    poem_stripped = [line.strip() for line in poem_listed]
    print(poem_stripped[0])
    for i in range(1, len(poem_stripped)-1):
        if poem_stripped[i] == '':
            continue
        if poem_stripped[i-1] == '':
            print(poem_stripped[i])
        if poem_stripped[i-1] != '':
            print(INDENTS * ' ' + poem_stripped[i])

    # for line in poem_stripped:
    #     print(line)
#
# def poem_divider(poem):
#     if ' ' in poem:


print_hanging_indents("""
                      Remember me when I am gone away,
                      Gone far away into the silent land;
                      When you can no more hold me by the hand,

                      Nor I half turn to go yet turning stay.

                      Remember me when no more day by day
                      You tell me of our future that you planned:
                      Only remember me; you understand
                      """)


