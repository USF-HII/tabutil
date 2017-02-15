# CusteomH Testeelper Functions
from test_helper import *

# Utility libraries
import io
import sys

# Class/Module Under Test
import tabutil.core

def create_input_file(*rows):
    f = io.StringIO()
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

        input_file_b = create_input_file(
            [ 'ID',    'Teddy4', 'Teddy5', 'Teddy6' ],
            [ 'TXNIP', '70',     'grape',   '60' ],
            [ 'GCL6',  '30',     'orange',  '10' ],
            [ 'GOS2',  '50',     'zulu',    '90' ]
        )

        input_file_c = create_input_file(
            [ 'ID', 'Teddy4',  'Teddy5', 'Teddy6' ],
            [ 'XYZ', '70',     'grape', '60' ],
            [ 'ABC', '30',     'orange', '10' ],
            [ 'GEF', '50',     'zulu',   '90' ]
        )

        input_file_d = create_input_file(
            [ 'ID',    'Teddy1', 'Teddy2', 'Teddy3' ],
            [ 'TXNIP', '',       'apple',  '29'     ],
            [ 'GCL6',  '56',     'baker',  '99'     ],
            [ 'GOS2',  '77',     'apple',  ''       ],
            [ 'INS',   '3',      'echo',   '54'     ]
        )


        self.df = pd.read_csv(input_file, sep='\t', index_col=0, dtype=str)
        self.df_b = pd.read_csv(input_file_b, sep='\t', index_col=0, dtype=str)
        self.df_c = pd.read_csv(input_file_c, sep='\t', index_col=0, dtype=str)
        self.df_d = pd.read_csv(input_file_d, sep='\t', index_col=0, dtype=str)

    def test_column_extract(self):
        result = tabutil.core.column_extract(self.df, ['Teddy1', 'Teddy3'])

        expected = create_csv(
            [ 'ID',    'Teddy1', 'Teddy3' ],
            [ 'TXNIP', '42',     '29' ],
            [ 'GCL6',  '56',     '99' ],
            [ 'GOS2',  '77',     '100' ],
            [ 'INS',   '3',      '54' ]
        )

        assert_equals(result, expected)

    def test_col_append(self):
        result = tabutil.core.column_append(self.df, self.df_b)

        expected = create_csv(
                       [ 'ID',       'Teddy1',    'Teddy2',    'Teddy3',  'Teddy4',    'Teddy5',    'Teddy6' ],
                       [ 'GCL6',     '56',        'baker',     '99',      '30',        'orange',    '10'     ],
                       [ 'GOS2',     '77',        'apple',     '100',     '50',        'zulu',      '90'     ],
                       [ 'INS',      '3',         'echo',      '54',      '',          '',          ''       ],
                       [ 'TXNIP',    '42',        'apple',     '29',      '70',        'grape',     '60'     ],
                   )

        assert_equals(result, expected)

    def test_row_extract_match(self):
        result = tabutil.core.row_extract_match(self.df, 'Teddy2', 'apple')

        expected = create_csv(
            [ 'ID',    'Teddy1', 'Teddy2', 'Teddy3' ],
            [ 'TXNIP', '42',     'apple',  '29'     ],
            [ 'GOS2',  '77',     'apple',   '100'   ]
        )

        assert_equals(result, expected)

    def test_row_extract(self):
        result = tabutil.core.row_extract(self.df, ['TXNIP', 'GCL6'])

        expected = create_csv(
            [ 'ID',    'Teddy1', 'Teddy2', 'Teddy3' ],
            [ 'TXNIP', '42',     'apple',  '29'     ],
            [ 'GCL6',  '56',     'baker',  '99'     ],
        )

        assert_equals(result, expected)

    def test_column_drop(self):
        result = tabutil.core.column_drop(self.df, ['Teddy1', 'Teddy3'])

        expected = create_csv(
            [ 'ID',    'Teddy2' ],
            [ 'TXNIP', 'apple'  ],
            [ 'GCL6',  'baker'  ],
            [ 'GOS2',  'apple'  ],
            [ 'INS',   'echo'   ]
        )

        assert_equals(result, expected)

    def test_row_drop(self):
        result = tabutil.core.row_drop(self.df, ['GCL6'])

        expected = create_csv(
            [ 'ID',    'Teddy1', 'Teddy2', 'Teddy3' ],
            [ 'TXNIP', '42',     'apple',  '29'     ],
            [ 'GOS2',  '77',     'apple',  '100'    ],
            [ 'INS',   '3',      'echo',   '54'     ]
        )

        assert_equals(result, expected)

    def test_column_rename(self):
        result = tabutil.core.column_rename(self.df, [('Teddy2', 'TeddyB'), ('Teddy1', 'TeddyA')])

        expected = create_csv(
            [ 'ID',    'TeddyA', 'TeddyB', 'Teddy3' ],
            [ 'TXNIP', '42',     'apple',  '29'     ],
            [ 'GCL6',  '56',     'baker',  '99'     ],
            [ 'GOS2',  '77',     'apple',  '100'   ],
            [ 'INS',   '3',      'echo',   '54'     ]
        )

        assert_equals(result, expected)

    def test_row_rename(self):
        result = tabutil.core.row_rename(self.df, [('TXNIP', 'FOO')])

        expected =  create_csv(
            [ 'ID',    'Teddy1', 'Teddy2', 'Teddy3' ],
            [ 'FOO',   '42',     'apple',  '29'     ],
            [ 'GCL6',  '56',     'baker',  '99'     ],
            [ 'GOS2',  '77',     'apple',   '100'    ],
            [ 'INS',   '3',      'echo',   '54'     ]
        )

        assert_equals(result, expected)

    def test_row_append(self):
        result = tabutil.core.row_append(self.df, self.df_c)

        expected = create_csv(
            [ 'ID',    'Teddy1', 'Teddy2', 'Teddy3', 'Teddy4',  'Teddy5',  'Teddy6' ],
            [ 'ABC',   '',       '',       '',       '30',      'orange',  '10'     ],
            [ 'GCL6',  '56',     'baker',  '99',     '',        '',        ''       ],
            [ 'GEF',   '',       '',       '',       '50',      'zulu',    '90'     ],
            [ 'GOS2',  '77',     'apple',  '100',    '',        '',        ''       ],
            [ 'INS',   '3',      'echo',   '54',     '',        '',        ''       ],
            [ 'TXNIP', '42',     'apple',  '29',     '',        '',        ''       ],
            [ 'XYZ',   '',       '',       '',       '70',      'grape',   '60'     ],
        )

        assert_equals(result, expected)

    def test_cell_replace(self):
        result = tabutil.core.cell_replace(self.df, [('42', '2000'),('apple', 'eggplant')])

        expected =  create_csv(
            [ 'ID',    'Teddy1', 'Teddy2',    'Teddy3' ],
            [ 'TXNIP', '2000',   'eggplant',  '29'     ],
            [ 'GCL6',  '56',     'baker',     '99'     ],
            [ 'GOS2',  '77',     'eggplant',  '100'    ],
            [ 'INS',   '3',      'echo',      '54'     ]
        )

        assert_equals(result, expected)

    def test_row_drop_blank(self):
        result = tabutil.core.row_drop_blank(self.df_d)

        expected = create_csv(
            [ 'ID',    'Teddy1', 'Teddy2', 'Teddy3' ],
            [ 'GCL6',  '56',     'baker',  '99'     ],
            [ 'INS',   '3',      'echo',   '54'     ]
        )

        assert_equals(result, expected)


    def test_row_sort(self):
        result = tabutil.core.row_sort(self.df, 'TXNIP')

        expected = create_csv(
            [ 'ID',    'Teddy3', 'Teddy1', 'Teddy2' ],
            [ 'TXNIP', '29',     '42',     'apple'  ],
            [ 'GCL6',  '99',     '56',     'baker'  ],
            [ 'GOS2',  '100',    '77',     'apple'  ],
            [ 'INS',   '54',     '3',      'echo'   ]
        )

        assert_equals(result, expected)

    def test_column_sort(self):
        result = tabutil.core.column_sort(self.df, 'Teddy2')

        expected = create_csv(
            [ 'ID',    'Teddy1', 'Teddy2', 'Teddy3' ],
            [ 'TXNIP', '42',     'apple',  '29'     ],
            [ 'GOS2',  '77',     'apple',  '100'    ],
            [ 'GCL6',  '56',     'baker',  '99'     ],
            [ 'INS',   '3',      'echo',   '54'     ],
        )

        assert_equals(result, expected)

    def test_column_sort_numeric(self):
        result = tabutil.core.column_sort(self.df, 'Teddy3', numeric=True)

        expected = create_csv(
            [ 'ID',    'Teddy1', 'Teddy2', 'Teddy3' ],
            [ 'TXNIP', '42',     'apple',  '29'     ],
            [ 'INS',   '3',      'echo',   '54'     ],
            [ 'GCL6',  '56',     'baker',  '99'     ],
            [ 'GOS2',  '77',     'apple',  '100'    ]
        )

        assert_equals(result, expected)

