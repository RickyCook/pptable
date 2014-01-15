def getindex(lst, idx, default=None):
    """
    Get index from list, or default
    """
    try:
        return lst[idx]
    except IndexError:
        return default

def pprow(row, widths):
    """
    Print a table row, padding columns where necessary
    """
    print "| " + " | ".join(
        "{:{}}".format(col_val, widths[col_idx])
        for col_idx, col_val
        in enumerate(row)
    ) + " |"

def pptable(table):
    """
    Print a formatted table

    pptable([
        ('a', 'b', 'c'),
        ('aa', 'bb', 'cc'),
    ])

    | 0  | 1  | 2  |
    | a  | b  | c  |
    | aa | bb | cc |
    """
    max_cols = max(len(row) for row in table)
    col_indexes = xrange(0, max_cols)

    # Normalize the table columns
    table = [[getindex(row, idx, '') for idx in col_indexes]
             for row in table
             ]

    # Get col widths
    col_width = [max(len(row)
                     for row
                     in (i[j] for i in table)
                     )
                 for j in col_indexes
                 ]

    # Print header, data
    pprow(col_indexes, col_width)
    for row in table:
        pprow(row, col_width)