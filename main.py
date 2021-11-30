import read_data

df = read_data.read_data()
if df:
    print(df.printSchema())
    print("\n\n")
    print(df.show(5))
    print("\n\n")
    print(df.describe())
