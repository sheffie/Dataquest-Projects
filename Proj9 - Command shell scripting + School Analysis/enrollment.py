if __name__ == "__main__":
    import pandas as pd
    data = pd.read_csv("/dataCRDC2013_14.csv",encoding = "Latin-1")
    data["total_enrollment"] = data["TOT_ENR_M"] + data["TOT_ENR_F"]
    cols = ['SCH_ENR_HI_M',
    'SCH_ENR_HI_F',
    'SCH_ENR_AM_M',
    'SCH_ENR_AM_F',
    'SCH_ENR_AS_M',
    'SCH_ENR_AS_F',
    'SCH_ENR_HP_M',
    'SCH_ENR_HP_F',
    'SCH_ENR_BL_M',
    'SCH_ENR_BL_F',
    'SCH_ENR_WH_M',
    'SCH_ENR_WH_F',
    'SCH_ENR_TR_M',
    'SCH_ENR_TR_F']
    sumlist = {}
    for i in range(len(cols)):
        sumlist[cols[i]] = data[cols[i]].sum()
    print(sumlist)
    all_enrollment = data["total_enrollment"].sum()
    pprt_list = {}
    for key, value in sumlist.items():
        pprt_list[key] = value/all_enrollment
    print(pprt_list)
     
