import pandas as pd
import os
from typing import List

def format_output(directory: str, routes: dict[str: str]) -> pd.DataFrame:

    files = []

    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)

        if ".csv" in f:
            files.append(f)


    for route in routes.keys():
        route_data = {
                "Arrival Time": [],
                "Next Stop": [],
                "Arrival at Next Stop": [],
                "Days": []
        }
        for file in files:
        
            if str(route) in file:
                df = pd.read_csv(file)
                df = df.rename(columns=lambda x: x.strip())

                for i in range(len(df)):
                    route_data["Arrival Time"].append(df.loc[i, routes[route]])

                    if "Monday" in file:
                        route_data["Days"].append("Weekdays")
                    if "Saturday" in file:
                        route_data["Days"].append("Saturday")
                    if "Sunday" in file:
                        route_data["Days"].append("Sunday")

                    idx = list(df.columns).index(routes[route]) + 1

                    route_data["Next Stop"].append(df.columns[idx])
                    route_data["Arrival at Next Stop"].append(df.loc[i, df.columns[idx]])
        
        route_df = pd.DataFrame.from_dict(route_data)

        for col in route_df.columns:
            route_df = route_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
        
        route_df.to_csv(f"{route}_route.csv", index=False)

            
                    


                

if __name__ == "__main__":
    dir = "routes"
    routes = {"Williston": "University Heights",
              "Essex": "UVM Medical Center",
              "City": "UVM Waterman Building",
              "Airport": "UVM Medical Center"
              }

    df = format_output(dir, routes)
            


        
        



        
        