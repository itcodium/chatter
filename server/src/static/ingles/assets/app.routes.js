var APP_API= {
    // APP_URL: "http://127.0.0.1:5000/api/ingles/",
    APP_URL: "http://chatbot-chatbot01.7e14.starter-us-west-2.openshiftapps.com/api/ingles/",
    // APP_TOKEN: "uuid=a223e322-3657-11e6-a49b-c04a00011902",
    PHRASES: "phrases",
    CATEGORIES: "categories",
    getUrl: function (api,id) {
        console.log("+ Get Url + api, id ",api,id)
        if (typeof id!='undefined'){
            var url= this.APP_URL + this[api.toUpperCase()] + "/" + id ;
            console.log("+ URL +",this[api.toUpperCase()] + "/" + id )
            return url;
        } else {

            var url=this.APP_URL + this[api.toUpperCase()]
            console.log("+ ELSE URL + ",this[api.toUpperCase()])
            
            return url;
        }
    }
};

