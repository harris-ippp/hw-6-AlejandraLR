# q2 Loop over your list from Part 1, and use requests to download the CSV files from.
import requests
#loop over a file
for line in open("ELECTION_ID"):
    addr=addr="http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0".format(line[5:10])
    resp=requests.get(addr)
    s=resp.status_code
    print(s)
#print contents of response
    file_name = line[0:4] +".csv" #saving it as year.csv as it saves extra line of codes for me in the next question. For naming it per the question the code:file_name = "president_general_"+line[0:4] +".csv"
    with open(file_name, "w") as out:
        out.write(resp.text)
