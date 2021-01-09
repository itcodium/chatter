from flask import jsonify
from .support_jsonp import support_jsonp_error

class CustomException():
    def showCustomException(self,err,parameters):
        status=500
        if len(err.args)==1:
            if str(type(err))=="<class 'NameError'>":
                data={"status":"ERROR", "message": str(err).replace("'","")}
            else:    
                data={"status":"ERROR", "message": err.args[0]}

            return support_jsonp_error(data,parameters)
        if len(err.args)>1:
            if err.args[1]=="A0000":
                status=401
        data={"status":"ERROR", "message": err.args[0],"error_code": err.args[1]}
        error_data= jsonify(data) 
        return support_jsonp_error(data,parameters) # 

