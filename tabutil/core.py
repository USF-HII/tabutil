def extract_columns(df, *columns):
    return(df.loc[:, columns].to_csv(sep='\t'))

def extract_rows(df, column_name, value):
    return(df.loc[df[column_name] == value].to_csv(sep='\t'))

def remove_columns(df, *column_names):
    for column_name in column_names:
        df.drop(column_name, axis=1, inplace=True)
    return(df.to_csv(sep='\t'))

def remove_rows(df, *row_ids):
    for row_id in row_ids:
        df.drop(row_id, inplace=True)
    return(df.to_csv(sep='\t'))

def replace_column_headers(df, *rename_pairs):
    for rename_pair in rename_pairs:
        df.rename(columns={rename_pair[0]: rename_pair[1]}, inplace=True)
    return(df.to_csv(sep='\t'))

def replace_row_ids(df, *rename_pairs):
    for rename_pair in rename_pairs:
        df.rename(index={rename_pair[0]: rename_pair[1]}, inplace=True)
    return(df.to_csv(sep='\t'))

