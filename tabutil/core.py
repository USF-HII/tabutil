import pandas as pd

def column_extract(df, columns, separator='\t'):
    return df.loc[:, columns].to_csv(sep=separator, index=False)

def column_extract_with_index(df, columns, separator='\t'):
    return df.loc[:, columns].to_csv(sep=separator)

def column_drop(df, column_names, separator='\t'):
    for column_name in column_names:
        df.drop(column_name, axis=1, inplace=True)
    return df.to_csv(sep=separator)

def column_rename(df, rename_pairs, separator='\t'):
    for rename_pair in rename_pairs:
        df.rename(columns={rename_pair[0]: rename_pair[1]}, inplace=True)
    return df.to_csv(sep=separator)

def column_append(df, df2, separator='\t'):
    appended_df = df.join(df2, how='outer')
    return appended_df.to_csv(sep=separator)

def row_extract(df, row_ids, separator='\t'):
    return df.filter(items=row_ids, axis='index').to_csv(sep=separator)

def row_extract_match(df, column_name, value, separator='\t'):
    return df.loc[df[column_name] == str(value)].to_csv(sep=separator)

def row_drop(df, row_ids, separator='\t'):
    for row_id in row_ids:
        df.drop(row_id, inplace=True)
    return df.to_csv(sep=separator)

def row_rename(df, rename_pairs, separator='\t'):
    for rename_pair in rename_pairs:
        df.rename(index={rename_pair[0]: rename_pair[1]}, inplace=True)
    return df.to_csv(sep=separator)

def row_append(df1, df2, separator='\t'):
    df = pd.concat([df1, df2], axis=1).fillna('')
    df.index.name = df1.index.name
    return df.to_csv(sep=separator)

def row_drop_blank(df, separator='\t'):
    df.dropna(how='any', inplace=True)
    return df.to_csv(sep=separator)

def row_sort(df, row_id, numeric=False, separator='\t'):
    if numeric:
        df.loc[row_id] = df.loc[row_id].apply(pd.to_numeric)
    columns = df.ix[row_id]
    return df[columns.argsort()].to_csv(sep=separator)

def column_sort(df, column_name, numeric=False, separator='\t'):
    if numeric:
        df[[column_name]] = df[[column_name]].apply(pd.to_numeric)
    return df.sort_values(column_name).to_csv(sep=separator)

def cell_replace(df, changesets, separator='\t'):
    for changeset in changesets:
        df.replace(changeset[0], changeset[1], inplace=True)
    return df.to_csv(sep=separator)

def get_sets(df1, df2, mode):
    if mode == 'row':
        a = set(df1.index)
        b = set(df2.index)
    if mode == 'column':
        a = set(df1.columns)
        b = set(df2.columns)
    return a, b

def set_intersect(df1, df2, mode):
    a, b = get_sets(df1, df2, mode)
    return sorted(a.intersection(b))

def set_union(df1, df2, mode):
    a, b = get_sets(df1, df2, mode)
    return sorted(a.union(b))

def set_diff(df1, df2, mode):
    a, b = get_sets(df1, df2, mode)
    return sorted(a.difference(b))

def set_sym_diff(df1, df2, mode):
    a, b = get_sets(df1, df2, mode)
    return sorted(a.symmetric_difference(b))
