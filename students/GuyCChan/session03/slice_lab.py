""" swap the first and last elements in a string and a tuple """
def exch_first_last():
    a_string = "this is a string"
    mid_st = a_string[1:-1]
    a_st_b_f = a_string[-1] + mid_st + a_string[0]
    print("This is a swapped string: " + a_st_b_f)
    a_tup = (2, 65, 13, 12, 11, 5, 37)
    mid_tup = a_tup[1:-1]
    a_tup_b_to_f = (a_tup[-1],) + mid_tup + (a_tup[0],)
    print(a_tup_b_to_f)

""" remove every other item in a sequence """
def rem_ev_oth():
    b_string = "This is not a very long string"
    b_srn = b_string[::2]
    print(b_srn)

""" remove the first 4 and last 4 items, and then every other item in the remaining """
def rem_fi_la_4():
    c_string = "This is not long but a fun string"
    c_ti = c_string[4:-4:2]
    print(c_ti)

""" reverse the elements with slicing """
def rev_el():
    d_string = "This is another string"
    d_str_rev = d_string[::-1]
    print(d_str_rev)

""" put in the oreder of: last third, first third, then middle third """
def las_fir_mid():
    e_string = "I need this string to be longer"
    print(len(e_string))
    l_f_m_str = e_string[-10:] + e_string[:21]
    print(l_f_m_str)


"""
if __name__ == "__main__":
    exch_first_last()
    rem_ev_oth()
    rem_fi_la_4()
    rev_el()
    las_fir_mid()
"""