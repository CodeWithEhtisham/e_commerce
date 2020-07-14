import numpy as np
import pandas as pd
import json
from pathlib import Path


def json_parser():
        base_path = Path(__file__).parent
        file_path = (base_path / "../data/label.json").resolve()
        with open(file_path) as f:
            data = json.load(f)
            # print(data)
            # trend=random.sample(range(0, 300), 60)
            my_data=[]
            for key in data:
                store=data[key]["data"]
                for value in store:
                    my_data.append([value["id"],value['itemTitle'],
                    value["itemImg"],value["itemPackageSize"],value["itemPrice"]+"$",value['itemReviews'],value["itemRatingScore"]])

            df=pd.DataFrame(data=my_data,columns=["id","title","img","size","price","reviews","rating"])
            print(df.shape)
            file=(base_path / "../data/train.csv").resolve()
            df.to_csv(file,index=False)


if __name__ == "__main__":
    json_parser()
