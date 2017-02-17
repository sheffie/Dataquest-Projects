if __name__ == "__main__":
    import pandas as pd
    data = pd.read_csv("/data/CRDC2013_14.csv",encoding = "Latin-1")
    vcounts_JJ = data["JJ"].value_counts()
    vcounts_SCHSM = data["SCH_STATUS_MAGNET"].value_counts()
    print(vcounts_JJ)
    print(vcounts_SCHSM)
    pt_JJ = pd.pivot_table(data, values=["TOT_ENR_M", "TOT_ENR_F"], index="JJ", aggfunc="sum")
    pt_SCHSM = pd.pivot_table(data, values=["TOT_ENR_M", "TOT_ENR_F"], index="SCH_STATUS_MAGNET", aggfunc="sum")
    print(pt_JJ)
    print(pt_SCHSM)
	
