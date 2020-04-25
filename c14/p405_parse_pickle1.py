import pickletools

from file_path_collect import output_pickle_path_dir as output

with open(output + 'entry.pickle', 'rb') as f:
    pickletools.dis(f)

"""
    0: \x80 PROTO      3
    2: }    EMPTY_DICT
    3: q    BINPUT     0
    5: (    MARK
    6: X        BINUNICODE 'title'
   16: q        BINPUT     1
   18: X        BINUNICODE 'Divve into history, 2009 edition'
   55: q        BINPUT     2
   57: X        BINUNICODE 'article_link'
   74: q        BINPUT     3
   76: X        BINUNICODE 'http://diveintomark.org/archives/2009/03/27/dive‐into‐history‐2009‐edition'
  163: q        BINPUT     4
  165: X        BINUNICODE 'comments_link'
  183: q        BINPUT     5
  185: N        NONE
  186: X        BINUNICODE 'internal_id'
  202: q        BINPUT     6
  204: C        SHORT_BINBYTES b'\xde\xd5\xb4\xf8'
  210: q        BINPUT     7
  212: X        BINUNICODE 'tags'
  221: q        BINPUT     8
  223: X        BINUNICODE 'diveintopython'
  242: q        BINPUT     9
  244: X        BINUNICODE 'docbook'
  256: q        BINPUT     10
  258: X        BINUNICODE 'html'
  267: q        BINPUT     11
  269: \x87     TUPLE3
  270: q        BINPUT     12
  272: X        BINUNICODE 'published'
  286: q        BINPUT     13
  288: \x88     NEWTRUE
  289: X        BINUNICODE 'published_date'
  308: q        BINPUT     14
  310: c        GLOBAL     'time struct_time'
  328: q        BINPUT     15
  330: (        MARK
  331: M            BININT2    2009
  334: K            BININT1    3
  336: K            BININT1    27
  338: K            BININT1    22
  340: K            BININT1    20
  342: K            BININT1    42
  344: K            BININT1    4
  346: K            BININT1    86
  348: J            BININT     -1
  353: t            TUPLE      (MARK at 330)
  354: q        BINPUT     16
  356: }        EMPTY_DICT
  357: q        BINPUT     17
  359: (        MARK
  360: X            BINUNICODE 'tm_zone'
  372: q            BINPUT     18
  374: N            NONE
  375: X            BINUNICODE 'tm_gmtoff'
  389: q            BINPUT     19
  391: N            NONE
  392: u            SETITEMS   (MARK at 359)
  393: \x86     TUPLE2
  394: q        BINPUT     20
  396: R        REDUCE
  397: q        BINPUT     21
  399: u        SETITEMS   (MARK at 5)
  400: .    STOP
highest protocol among opcodes = 3
"""
