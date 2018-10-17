import json

class ValidateLogin:
    def run(elem):
        # elem=LoginWithValidDetails.test(self)
        # elem = LoginWithValidDetails.test(elem)
        creds = open("C:\\Users\\SANTOSH\\PycharmProjects\\PythonAction\\test_suit\\functional\\json\\credentials.json", "r",
                        encoding="utf-8")
        credentials = json.load(creds)
        if (elem == credentials['Credentials']['sa']):
            return "Test Case Verified Successfully"
        else:
            return "Test Case Failed Successfully"
        creds.close()