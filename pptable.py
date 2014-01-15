def getindex(lst, idx, default=None):
    """
    Get index from list, or default
    """
    try:
        return lst[idx]
    except IndexError:
        return default

def print_row(row, widths):
    """
    Print a table row, padding columns where necessary
    """
    print "| " + " | ".join(
        "{:{}}".format(col_val, col_width[col_idx])
        for col_idx, col_val
        in enumerate(row)
    ) + " |"

def print_table(table):
    """
    Print a formatted table

    print_table([
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
    print_row(col_indexes, col_width)
    for row in table:
        print_row(row, col_width)