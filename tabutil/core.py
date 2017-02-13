def column_extract(df, *columns):
    return(df.loc[:, columns].to_csv(sep='\t'))

def column_drop(df, *column_names):
    for column_name in column_names:
        df.drop(column_name, axis=1, inplace=True)
    return(df.to_csv(sep='\t'))

def column_rename(df, *rename_pairs):
    for rename_pair in rename_pairs:
        df.rename(columns={rename_pair[0]: rename_pair[1]}, inplace=True)
    return(df.to_csv(sep='\t'))

def column_append(df, df2):
    appended_df = df.join(df2, how='outer')
    return(appended_df.to_csv(sep='\t'))

def row_extract(df, *row_ids):
    separator='\t'
    return(df.filter(items=row_ids, axis='index').to_csv(sep=separator))

def row_extract_match(df, column_name, value):
    return(df.loc[df[column_name] == str(value)].to_csv(sep='\t'))

def row_drop(df, *row_ids):
    for row_id in row_ids:
        df.drop(row_id, inplace=True)
    return(df.to_csv(sep='\t'))

def row_rename(df, rename_pairs):
    for rename_pair in rename_pairs:
        df.rename(index={rename_pair[0]: rename_pair[1]}, inplace=True)
    return(df.to_csv(sep='\t'))

