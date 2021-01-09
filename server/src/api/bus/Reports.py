from api.data import Reports

class Reports():
    def get(self):
        report=Reports()
        return report.get() 