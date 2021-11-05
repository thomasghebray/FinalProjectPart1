#Student Name: Thomas Ghebray
#PSID: 1889967

import pandas as pd
import numpy as np
from functools import reduce


from pandas.io.pytables import IncompatibilityWarning

"""
# TODO:
# install pandas and numpy
// on your env

$ pip install pandas
$ pip install numpy

// run file
> python inv_manager.py


## 1.Load in files: 
 ### ```1. ManufacturerList.csv columns=[item_ID,Manufucturer_name,item_type,indicator]```
 ### ```2. PriceList.csv columns=[item_ID,item_price]```
 ### ```3. ServiceDatesList.csv columns=[item_ID,Dates]```

# Required to work with any group of input files of csv 
"""



class InventoryManager:
    def __init__(self,data1,data2,data3):
        # load file paths
        """
            LOAD IN FILE PATH OF THE DATA INTO THE 
            CLASS, WHICH WILL BE CALLED BY OTHER 
            FUNCTIONS TO OUTPUT OUR DATA.

            TO LOAD A PATH TUTORIOL:
                -- create a path variable:
                path_1 = "../manufacturelist.csv"
                path_2 = "../pricelist.csv"
                path_3 = "../servicedatelist.csv"

                # load them into our class
                # first create its instance
                inventory = InventoryManager(path_1,path_2,path_3)

                # get outputs:
                    inventory.fullinventory() #-- gives you a csv of the full inventory

        """
        self.df_manuf_list = data1
        self.df_price_list = data2
        self.df_serv_date_list = data3
    
    def data_loader(self):
        # create pandas data frame of the loaded files:
        # rename columns of the loaded files
        try:
            manufacture_list = pd.read_csv(self.df_manuf_list, names=['item_ID','Manufucturer_name','item_type','indicator']) 
            price_list = pd.read_csv(self.df_price_list, names=['item_ID','item_price'])
            Service_Date_list = pd.read_csv(self.df_serv_date_list,names=['item_ID','Dates'])
        except:
            print("---SORRY SEEMS THE FILES ARE MISSING \n\t ARE YOU SURE THE FILE PATH WAS CORRECT?---")

        return manufacture_list,price_list,Service_Date_list
    
    def full_inventory(self):
        """
        return new dataframe containing only those rows that 
        have a matching value in both original dataframes.
        """
        # get loaded files:
        df_manufacturer, df_prices, df_service_dates = self.data_loader()

        # since we have a similar column calles item_ID we can merge on that
        # an inner join on the item_ID column will be our best bet 
        # as each item has a unique id


        # should return output file in csv format
        dfs = [df_manufacturer,df_prices,df_service_dates]
        #output_1 = pd.merge(df_manufacturer, df_prices,on='item_ID',how='inner')

        #output = pd.merge(output_1,df_service_dates,on="item_ID",how="inner")
        df_final = reduce(lambda left,right: pd.merge(left,right,on='item_ID'), dfs)

        output = df_final.copy(deep=True)

        # sort the values 
        output.sort_values(by=['Manufucturer_name'],inplace=True)
        return output.to_csv("full_inventory.csv")
        

    def item_type_inventory(self):
        # load files
        df_manufacturer, df_prices, df_service_dates = self.data_loader()
        pass
    
    def past_service_inventory(self):
        # load files
        df_manufacturer, df_prices, df_service_dates = self.data_loader()
        pass
    
    def damaged_inventory(self):
        # load files
        df_manufacturer, df_prices, df_service_dates = self.data_loader()
        pass


# create file paths here I.E

path1 = "../ManufacturerList(3).csv"
path2 = "../PriceList(1).csv"
path3 = "../ServiceDatesList(3).csv"

# CREATE CLASS INSTANCE

inventory = InventoryManager(path1,path2,path3)

# output files 
if __name__ == '__main__':
    inventory.full_inventory() # full inventory
