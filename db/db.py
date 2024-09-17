import mysql.connector 
import json


class SmartInsuranceDatabase:
    def __init__(self):
        self.mydb=mysql.connector.connect(
        host="localhost", 
        user="root", 
        password="password",
        database="smartinsurance")
        self.cur=self.mydb.cursor()

    def get_all_serviceprovider(self):
        #using store procedure
        self.cur.callproc('GetAllServiceProviders')
        data = {'serviceProviderDetails':[]}
        for result in self.cur.stored_results():
            rows = result.fetchall()  # Fetch all rows
        for row in rows:
            result={"provider_id":row[0], 'name':row[1], 'provider_type':row[2], 'region_id':row[3], 'status':row[4], 'no_of_claims':row[5]}
            data['serviceProviderDetails'].append(result)

        # json_data = json.dumps(data, indent=4)
        return(data)


        
        # Convert the result list into JSON format

        self.cur.close()
        self.mydb.close()


if __name__=='__main__':
    obj=SmartInsuranceDatabase()
    result=obj.get_all_serviceprovider()
    print(result)
