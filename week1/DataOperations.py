from pickle import APPEND, NONE
import numpy as np
import pandas as pd
import seaborn as sns

class DataOperations:
    """ 
        Attributes: to_do : determine operations(csv path, narray,dataframe,empty(for random dataframe)) default:empty
                    random_data_row:row count for random genareted dataframe default:100
                    random_data_column:column count for random genareted dataframe default:2
                    Range:number of range for random genareted dataframe default:100
        You can use DataOperations class for generate dataframe and visualize the dataframe
        To use generate DataFrame You have 4 Option
        1-If you want to transform your nparray to dataframe call DataOperations() and pass your narray as an argument
        2-You can pass your csv file path as an argument
        3-You can give your dataframe to create DataOperations() object to use visualization function
        4-You can just call DataOperations() with no argument dataframe is genarated randomly( You can change the column and row size in DataOperations.py
        
        Format: your_object_name.dataframe
        Visuatilion functions:
        1-you can use  swarmplot function for Visuatilion
            Format: Your_object_name.swarmplot(Column_name,Column_name2)
            you are expected to give two column name in your dataset
        2-boxplot
         Format: Your_object_name.swarmplot(Column_name)
            you are expected to give two column name in your dataset
        """
    dataframe=pd.DataFrame()
    
   
    
    
    def __init__(self,to_do=NONE, random_data_row=100,random_data_column=2,Range=100) -> None:
        
        if(type(to_do).__module__ == np.__name__):
        
            column_count=to_do.shape[1]
            columns=[]
            for i in range(1,column_count+1):
                colum_name="Column_"
                colum_name+=str(i)
                columns.append(colum_name)
                
            self.dataframe = pd.DataFrame(to_do, columns = columns)
        elif(type(to_do)==str):
            
            self.dataframe = pd.read_csv(to_do)
         

        elif(type(to_do) == pd.DataFrame):
            
            self.dataframe=to_do

        elif(to_do is NONE):

            columns=[]
            for i in range(1,random_data_column+1):
                colum_name="Column_"
                colum_name+=str(i)
                columns.append(colum_name)
            self.dataframe=pd.DataFrame(np.random.rand(random_data_row,random_data_column)*Range
            ,columns=columns)

            
    def boxplot(self,column=NONE):
        """ Only work for numerics value 
        This function aim to visualize given colum with boxplot to see outlier
        """
        if column  not in  self.dataframe:
            print("Your dataframe dont have  a column named ", column)
            return 
        else:
            sns.boxplot(self.dataframe[column])
    def swarmplot(self,column_1=NONE,column_2=NONE):
        """ This function aim to visualize given columns with swamplot
            Paramaters:
            column_1: x_edge 
            column_2:y edge"""
        if column_1 is NONE or column_2 is NONE:
            print("You must give 2 column name to use swamrplot")
        if column_1  not in  self.dataframe: 
            print("Your dataframe dont have  a column named ", column_1)
            return 
        if  column_2 not in self.dataframe:
            print("Your dataframe dont have  a column named ", column_2)
            return 
        sns.swarmplot(x=column_1, 
              y=column_2,
              data=self.dataframe)
   
        

        
        
