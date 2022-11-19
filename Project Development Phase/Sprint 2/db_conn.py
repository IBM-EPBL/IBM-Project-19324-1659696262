import ibm_db as db
 
class DbConn:
    
    def __init__(self):
        self.DATABASE = "bludb"
        self.HOSTNAME = "8e359033-a1c9-4643-82ef-8ac06f5107eb.bs2io90l08kqb1od8lcg.databases.appdomain.cloud"
        self.PORT = "30120"
        self.SECURITY = "SSL"
        self.CERTIFICATE = "DigiCertGlobalRootCA.crt"
        self.USR_ID = "bbr24632"
        self.PWD = "IBEoOkRVWT7nV9Fl"

        self.dsn =(
                "DATABASE={0};"
                "HOSTNAME={1};"
                "PORT={2};"
                "SECURITY={3};"
                "SSLServerCertificate={4};"
                "UID={5};"
                "PWD={6};"
        ).format(self.DATABASE,self.HOSTNAME,self.PORT,self.SECURITY,self.CERTIFICATE,self.USR_ID,self.PWD)

    def connect(self):

        dsn = self.dsn
        try:
            conn = db.connect(dsn,"","")
            print("Connection Successfull")
            return conn

        except:

            print("Unable to connect:",db.conn_errormsg())
