## Write Pandas DataFrame into a MySQL Database Table ##
from sqlalchemy import create_engine
import pymysql
import pandas as pd

userVitals = {"UserId":["xxxxx", "yyyyy", "zzzzz", "aaaaa", "bbbbb", "ccccc", "ddddd"],
              "UserFavourite":["Greek Salad", "Philly Cheese Steak", "Turkey Burger", "Crispy Orange Chicken", "Atlantic Salmon", "Pot roast", "Banana split"],
              "MonthlyOrderFrequency":[5, 1, 2, 2, 7, 6, 1],
              "HighestOrderAmount":[30, 20, 16, 23, 20, 26, 9],
              "LastOrderAmount":[21,20,4,11,7,7,7],
              "LastOrderRating":[3,3,3,2,3,2,4],
              "AverageOrderRating":[3,4,2,1,3,4,3],
              "OrderMode":["Web", "App", "App", "App", "Web", "Web", "App"],
              "InMedicalCare":["No", "No", "No", "No", "Yes", "No", "No"]};

tableName = "UserVitals"
dataFrame = pd.DataFrame(data=userVitals)

sqlEngine = create_engine('mysql+pymysql://root:@127.0.0.1/test', pool_recycle=3600)
dbConnection = sqlEngine.connect()

try:
    frame = dataFrame.to_sql(tableName, dbConnection, if_exists='fail');
except ValueError as vx:
    print(vx)
except Exception as ex:
    print(ex)
else:
    print("Table %s created successfully."%tableName);
finally:
    dbConnection.close()



## Read a MySQL Database Table into a Pandas DataFrame ##
from sqlalchemy import create_engine
import pymysql
import pandas as pd

sqlEngine       = create_engine('mysql+pymysql://root:@127.0.0.1', pool_recycle=3600)
dbConnection    = sqlEngine.connect()
frame           = pd.read_sql("select * from test.uservitals", dbConnection);

pd.set_option('display.expand_frame_repr', False)

print(frame)

dbConnection.close()
