import pandas as pd

test = pd.read_csv("liga.csv")
#test = pd.read_csv("1.csv", usecols=["Nome", "Valor"])

df = pd.DataFrame(test)

print(df.head())

#new = df["Nome"].str.split(r"\n", n=-1)
#new = df['Nome']=df['Nome'].str.replace(r"\n", " ", regex=True)
#new = df['Nome']=df['Nome'].str.join(r'&&').str.replace(r"\n", "").str.split(r'&&')

df = df.join(df["Nome"].str.strip("'\"[]").str.split(r'\\n', expand=True))

df.rename(columns={0:"PT", 1:"EN"}, inplace=True)

#df["PT"] = df["Nome"].apply(lambda x: x[2:-2].split("\\n")[0])
#df["EN"] = df["Nome"].apply(lambda x: x[2:-2].split("\\n")[1:2])
df['Valor']=df['Valor'].apply(lambda x: x[2:-2])

df.drop(columns=["Nome"], inplace=True)

#df.to_csv("liga.csv")
print(df.head())