var API_METHOD = {
    ADD: "ADD",
    EDIT: "EDIT",
    DELETE: "DELETE"
}

 var ApiCaller=function () {
     
    var _params={};
    // this.apiName="";
    var apiName;
    var get_callback;
    var put_callback;
    var post_callback;
    var delete_callback;

    var scope={};
    _this=this;

    this.setRoute=function(param){
        apiName=param;
    }
    this.setScope=function(param){
        scope=param;
    }
    this.getScope=function(){
        return scope;
    }

    this.setCaller = function (param) {
        if (typeof this.caller == 'undefined') {
            this.caller = param;
        }
    }
    this.error = function (res) {
        alert("Error")
        console.log("error", res)
    }
    this.isError = function (res) {
        console.log("isError -> ", res)   
        var result = false;
        if (res.data.status.toUpperCase() == "ERROR") {
            alert("Error:  "+ res.data.message)
            result = true;
        }
        return result;
    }
    
    this.get = function (params,callback) {
        _params=params;
        var url=APP_API.getUrl(apiName);
        if(typeof callback!='undefined'){
            get_callback=callback;
        }
        this.caller.get(url, typeof _params=='undefined'?{}:_params)
            .then(get_callback, this.error)
    }

    this.getById = function (id,params,callback) {
        _this.params=params;
        _this.id=id;
        this.caller.get(APP_API.getUrl(apiName, _this.id), _this.params)
            .then(callback, this.error)
    }
    
    this.put = function (id,data,callback) {
        if(typeof callback!='undefined'){
            put_callback=callback;
        }
        var url=APP_API.getUrl(apiName, id);
        this.caller.put(url, data)
            .then(put_callBack, this.error)
    }

    
    this.post = function (data, callback) {
        console.log("POST", apiName)
        if(typeof callback!='undefined'){
            post_callback=callback;
        }
        var url=APP_API.getUrl(apiName);
        this.caller.post( url, data)
            .then(post_callback, this.error)
    }
   
    this.delete = function (id, callback) {
        if(typeof callback!='undefined'){
            delete_callback=callback;
        }
        
        console.log("DELETE", apiName)

        var url=APP_API.getUrl(apiName, id);
        this.caller.delete(url, {})
            .then(delete_callback, this.error)
    }
    
    var get_callback=function(res) {
        scope.modalEdit.items = res.data;
    }

    var put_callBack =function(res) {
        console.log("Put_callBack -> ",res)
        if (!scope.api.isError(res)) {
            if (res.status != 200) {
                alert(res.message);
            } else {
                scope.modalEdit.hide();
                console.log("PUT params",_params)

                if(typeof _params=='undefined'){
                    scope.api.get();    
                }else{
                    scope.api.get(_params,undefined);
                }
            }
        }
    }

     var post_callback = function (res) {
        console.log("Post_callBack -> ",res)
        if (!scope.api.isError(res)) {
            if (res.status != 200) {
                alert(res.message);
            } else {
                scope.modalEdit.hide();
                console.log("POST params",_params)
                if(typeof _params=='undefined'){
                    scope.api.get();    
                }else{
                    scope.api.get(_params,undefined);
                }
            }
        }
    }
  
   var delete_callback = function (res) {
        console.log("Post_callBack -> ",res)
        if (!scope.api.isError(res)) {
            if (res.status != 200) {
                alert(res.message);
            } else {
                scope.modalEdit.hide();
                console.log("DELETE params",_params)
                if(typeof _params=='undefined'){
                    scope.api.get();    
                }else{
                    scope.api.get(_params,undefined);
                }
            }
        }
    }

     /*
  
    this.Delete_callBack = function (res) {
        if (!_this.isError(res)) {
            if (res.status != 200) {
                alert(res.message);
            } else {
                scope.modalEdit.hide();
                _this.get();
            }
        }
    }
    */
};



 