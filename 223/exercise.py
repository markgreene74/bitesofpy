# https://codechalleng.es/bites/223/
def apply_conversion(single_rwx: str) -> str:
    """A small helper function that receives a single
       'rwx' string and convert it to the numeric
       representation.
    """
    conversion_table = {"r": 4, "w": 2, "x": 1, "-": 0}
    single_rwx_converted = sum([conversion_table.get(i) for i in single_rwx])
    return str(single_rwx_converted)


def get_octal_from_file_permission(rwx: str) -> str:
    """Receive a Unix file permission and convert it to
       its octal representation.

       In Unix you have user, group and other permissions,
       each can have read (r), write (w), and execute (x)
       permissions expressed by r, w and x.

       Each has a number:
       r = 4
       w = 2
       x = 1

       So this leads to the following input/ outputs examples:
       rw-r--r-- => 644 (user = 4 + 2, group = 4, other = 4)
       rwxrwxrwx => 777 (user/group/other all have 4 + 2 + 1)
       r-xr-xr-- => 554 (user/group = 4 + 1, other = 4)
    """
    split_str = [rwx[i : i + 3] for i in range(0, len(rwx), 3)]
    return "".join([apply_conversion(i) for i in split_str])

'''
Resolution time: ~31 min. (avg. submissions of 5-240 min.) - awesome, you solved it in 11 min. 💪
'''
