import pandas as pd
import glob
#get file names (fname) from the directory
fname=(glob.glob("*.csv"))
#create dataframe to contain files
dframe = pd.DataFrame()
#fix empty columns and column names and place all data frames in a list
list=[]
for file in fname:
    header = pd.read_csv(file, nrows = 1).dropna(axis = 1)
    d = header.iloc[0].to_dict()
    df= pd.read_csv(file, index_col = 0,
               thousands = ",", skiprows = [1])
    df.rename(inplace = True, columns = d)
    df.dropna(inplace = True, axis = 1)
    df["Year"] = file
    df["Year"] = df["Year"].replace(".csv", "", regex = True)
    df=df[["Democratic", "Republican", "Total Votes Cast", "Year"]]
    list.append(df)
    dframe=dframe.append(df)

#define new column for republican share of votes
dframe=dframe.groupby(['County/City', 'Year'])['Republican','Total Votes Cast'].sum().reset_index()
dframe['Republican Share']=dframe['Republican']/dframe['Total Votes Cast']
#plot the Republican vote share in Accomack County, Albermarle County, Alexandria City, and Alleghany County
# for Accomack
plot1=dframe[dframe["County/City"]=='Accomack County'].plot(x="Year", y="Republican Share")
plot1.get_figure().savefig('accomack_county.pdf')
# for Albemarle
plot2=dframe[dframe["County/City"]=='Albemarle County'].plot(x="Year", y="Republican Share")
# for Alexandria
plot3=dframe[dframe["County/City"]=='Alexandria City'].plot(x="Year", y="Republican Share")
plot3.get_figure().savefig('alexandria_city.pdf')
#for Alleghany
plot4=dframe[dframe["County/City"]=='Alleghany County'].plot(x="Year", y="Republican Share")
plot4.get_figure().savefig('alleghany_county.pdf')
