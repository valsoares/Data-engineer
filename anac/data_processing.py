import pandas as pd
from datetime import datetime

class Data:
    def __init__(self, path=None, dataframe=None):
        """
        Initializes a Data object with the provided file path.

        Parameters
        ----------
        path : str, optional
            The file path to be loaded.
        dataframe : pd.DataFrame, optional
            A DataFrame to initialize the Data object with.

        Raises
        ------
        ValueError
            If the file extension is not supported or neither path nor dataframe is provided.
        """
        if path:
            self.path = path
            self.type = path.split('.')[1]
            self.data = self.read_file()
        elif dataframe is not None:
            self.data = dataframe
        else:
            raise ValueError("Must provide either a file path or a DataFrame")
        
        self.remove_duplicates()
    
    def read_file(self):
        """
        Reads the file specified by `path` using the appropriate Pandas read function.

        Returns
        -------
        pd.DataFrame
            A Pandas DataFrame containing the loaded data.

        Raises
        ------
        ValueError
            If the file extension is not supported.
        """
        extension = {
        'csv': pd.read_csv,
        'txt': pd.read_table,
        'tsv': pd.read_table,
        'xls': pd.read_excel,
        'xlsx': pd.read_excel,
        'json': pd.read_json,
        'h5': pd.read_hdf,
        'hdf': pd.read_hdf,
        'parquet': pd.read_parquet,
        'feather': pd.read_feather,
        'pkl': pd.read_pickle,
        'sas7bdat': pd.read_sas,
        'sav': pd.read_spss,
        'dta': pd.read_stata,
        'orc': pd.read_orc,
        'xml': pd.read_xml
        }
        
        if self.type in extension:
            read_function = extension[self.type]
            return read_function(self.path, usecols=lambda column: column not in ["Unnamed: 0"])
        else:
            raise ValueError(f"Unsupported file extension: {extension}")
    
    def concat(self, other):
        """
        Concatenate the current Data object with another Data object.

        Parameters
        ----------
        other : Data
            The other Data object to concatenate with.

        Returns
        -------
        Data
            A new Data object with the concatenated DataFrame.
        """
        if not isinstance(other, Data):
            raise ValueError("The other object must be an instance of Data")
        
        concatenated_dataframe = pd.concat([self.data, other.data], ignore_index=True)
        return Data(dataframe=concatenated_dataframe)

    def remove_duplicates(self):
        self.data.drop_duplicates(inplace=True)
    
    def str_to_date(self, column, format):
        self.data[column] = pd.to_datetime(self.data[column], format=format, errors='coerce').dt.date
    
    def str_to_time(self, column, format):
        self.data[column] = pd.to_datetime(self.data[column], format=format, errors='coerce').dt.time
    
    def str_to_num(self, column):
        if self.data[column].str.contains(',').any():
            self.data[column] = self.data[column].str.replace(',', '.')
        self.data[column] = pd.to_numeric(self.data[column], errors='coerce')

    def join_date_time(self,date_column, time_column):
        self.data['DateTime'] = self.data.apply(lambda row: datetime.combine(row[date_column], row[time_column]), axis=1)