from flask import Flask, render_template
import pandas as pd
from datetime import datetime 


app = Flask(__name__)

@app.route('/')
def home():
    routes=[]
    time = datetime.now()
    day = datetime.today()
    today = day.isoweekday()
    df1=pd.read_csv("Airport_route.csv")
    df2=pd.read_csv("City_route.csv")
    df3=pd.read_csv("Essex_route.csv")
    df4=pd.read_csv("Williston_route.csv")

    if today < 5:
        df1 = df1[df1["Days"] == "Weekdays"]
    elif today == 5:
        df1 = df1[df1["Days"] == "Saturday"]
    elif today == 6:
        df1 = df1[df1["Days"] == "Sunday"]

    df1['Closest Stop Arrival Time'] = df1['Closest Stop Arrival Time'].map(lambda x: pd.to_datetime(x))
    df1['Arrival at Next Stop'] = df1['Arrival at Next Stop'].map(lambda x: pd.to_datetime(x))

    df1 = df1.sort_values(by=["Closest Stop Arrival Time"])
    df1 = df1[df1["Arrival at Next Stop"] > str(time)]


    data = {}
    for col in df1.columns:
        data[col]=df1[col].iloc[0]
    data['line'] = 'Airport Route'
    routes.append(data)



    if today < 5:
        df2 = df2[df2["Days"] == "Weekdays"]
    elif today == 5:
        df2 = df2[df2["Days"] == "Saturday"]
    elif today == 6:
        df2 = df2[df2["Days"] == "Sunday"]

    df2['Closest Stop Arrival Time'] = df2['Closest Stop Arrival Time'].map(lambda x: pd.to_datetime(x))
    df2['Arrival at Next Stop'] = df2['Arrival at Next Stop'].map(lambda x: pd.to_datetime(x))

    df2 = df2.sort_values(by=["Closest Stop Arrival Time"])
    df2 = df2[df2["Arrival at Next Stop"] > time]


    data = {}
    for col in df2.columns:
        data[col]=df2[col].iloc[0]
    data['line'] = 'City Route'
    routes.append(data)

    if today < 5:
        df3 = df3[df3["Days"] == "Weekdays"]
    elif today == 5:
        df3 = df3[df3["Days"] == "Saturday"]
    elif today == 6:
        df3 = df3[df3["Days"] == "Sunday"]

    df3['Closest Stop Arrival Time'] = df3['Closest Stop Arrival Time'].map(lambda x: pd.to_datetime(x))
    df3['Arrival at Next Stop'] = df3['Arrival at Next Stop'].map(lambda x: pd.to_datetime(x))

    df3 = df3.sort_values(by=["Closest Stop Arrival Time"])
    df3 = df3[df3["Arrival at Next Stop"] > str(time)]


    data = {}
    for col in df3.columns:
        data[col]=df3[col].iloc[0]
    data['line'] = 'Essex Route'
    routes.append(data)

    if today < 5:
        df4 = df4[df4["Days"] == "Weekdays"]
    elif today == 5:
        df4 = df4[df4["Days"] == "Saturday"]
    elif today == 6:
        df4 = df4[df4["Days"] == "Sunday"]

    df4['Closest Stop Arrival Time'] = df4['Closest Stop Arrival Time'].map(lambda x: pd.to_datetime(x))
    df4['Arrival at Next Stop'] = df4['Arrival at Next Stop'].map(lambda x: pd.to_datetime(x))

    df4 = df4.sort_values(by=["Closest Stop Arrival Time"])
    df4 = df4[df4["Arrival at Next Stop"] > str(time)]

    data = {}
    for col in df4.columns:
        data[col]=df4[col].iloc[0]
    data['line'] = 'Williston Route'
    routes.append(data)
   

    return render_template('index.html', data=routes)

if __name__ == '__main__':
    app.run(debug=True)
