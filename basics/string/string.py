# https://docs.python.org/3/library/stdtypes.html#string-methods


def main():
    s = "1234"
    # length
    print(len(s))
    # copy
    print(s[:])
    # backward index, till last char
    print(s[:-1])
    # slice, from second char and onward
    print(s[-2:])
    # repeat
    print(s * 3)
    # concatenation
    print(s + str(0))
    # raw type ignores backslash, can use u prefix too
    if s[:5] + s[5:] == s:
        print("s[:n] + s[n:] always partitions s, even out of bound")
    raw = r'this\t\n and that'
    print(raw)
    # multiline
    print("""\
        Usage: thingy [OPTIONS]
        -h                        Display this usage message
        -H hostname               Hostname to connect to
    """)
    # % operator to enable printf
    print("%d little pigs come out or I'll %s and %s and %s" %
          (3, 'huff', 'puff', 'blow down'))
    # unicode string is not the same as default byte str
    ustring = u'A unicode \u018e string \xf1'
    # unicode to byte
    bstring = ustring.encode('utf-8')
    # byte to unicode
    assert ustring == bstring.decode('utf-8')


if __name__ == '__main__':
    main()

# and or not
# elif
# ==, !=, <, <=, >, >=
