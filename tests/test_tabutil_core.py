# Custeom Test Helper Functions
from test_helper import *

# Utility libraries
import StringIO
import sys

# Class/Module Under Test
import tabutil.core

def create_input_file(*rows):
    f = StringIO.StringIO()
    for row in rows:
        f.write('\t'.join(row) + '\n')
    f.seek(0)
    return(f)

def create_csv(*rows):
    return('\n'.join(['\t'.join(row) for row in rows]) + '\n')

class TestTabUtil(unittest.TestCase):
    def setUp(self):
        import pandas as pd

        input_file = create_input_file(
            [ 'ID',    'Teddy1', 'Teddy2', 'Teddy3' ],
            [ 'TXNIP', '42',     'apple',  '29'     ],
            [ 'GCL6',  '56',     'baker',  '99'     ],
            [ 'GOS2',  '77',     'apple',  '100'    ],
            [ 'INS',   '3',      'echo',   '54'     ]
        )

        self.df = pd.read_csv(input_file, sep='\t', index_col=0)

    def test_extract_columns(self):
        result = tabutil.core.extract_columns(self.df, 'Teddy1', 'Teddy3')

        expected = create_csv(
            [ 'ID',    'Teddy1', 'Teddy3' ],
            [ 'TXNIP', '42',     '29' ],
            [ 'GCL6',  '56',     '99' ],
            [ 'GOS2',  '77',     '100' ],
            [ 'INS',   '3',      '54' ]
        )

        assert_equals(result, expected)

    def test_extract_rows(self):
        result = tabutil.core.extract_rows(self.df, 'Teddy2', 'apple')

        expected = create_csv(
            [ 'ID',    'Teddy1', 'Teddy2', 'Teddy3' ],
            [ 'TXNIP', '42',     'apple',  '29'     ],
            [ 'GOS2',  '77',     'apple',   '100'   ]
        )

        assert_equals(result, expected)

    def test_remove_columns(self):
        result = tabutil.core.remove_columns(self.df, 'Teddy1', 'Teddy3')

        expected = create_csv(
            [ 'ID',    'Teddy2' ],
            [ 'TXNIP', 'apple'  ],
            [ 'GCL6',  'baker'  ],
            [ 'GOS2',  'apple'  ],
            [ 'INS',   'echo'   ]
        )

        assert_equals(result, expected)

    def test_remove_rows(self):
        result = tabutil.core.remove_rows(self.df, 'GCL6')

        expected = create_csv(
            [ 'ID',    'Teddy1', 'Teddy2', 'Teddy3' ],
            [ 'TXNIP', '42',     'apple',  '29'     ],
            [ 'GOS2',  '77',     'apple',  '100'    ],
            [ 'INS',   '3',      'echo',   '54'     ]
        )

        assert_equals(result, expected)

    def test_replace_column_headers(self):
        result = tabutil.core.replace_column_headers(self.df, ('Teddy2', 'TeddyB'), ('Teddy1', 'TeddyA'))

        expected = create_csv(
            [ 'ID',    'TeddyA', 'TeddyB', 'Teddy3' ],
            [ 'TXNIP', '42',     'apple',  '29'     ],
            [ 'GCL6',  '56',     'baker',  '99'     ],
            [ 'GOS2',  '77',     'apple',  '100'   ],
            [ 'INS',   '3',      'echo',   '54'     ]
        )

        assert_equals(result, expected)

    def test_replace_row_id(self):
        result = tabutil.core.replace_row_ids(self.df, ('TXNIP', 'FOO'))

        expected =  create_csv(
            [ 'ID',    'Teddy1', 'Teddy2', 'Teddy3' ],
            [ 'FOO',   '42',     'apple',  '29'     ],
            [ 'GCL6',  '56',     'baker',  '99'     ],
            [ 'GOS2',  '77',     'apple',   '100'    ],
            [ 'INS',   '3',      'echo',   '54'     ]
        )

        assert_equals(result, expected)


