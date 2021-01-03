angular.module('app.services', [])
.service('AppServiceCaller', function ($http, $window, $httpParamSerializerJQLike) {

        var config = { headers: { 'Content-Type': 'application/x-www-form-urlencoded' } };

        var response = function (response) {
            return response;
        }
        var error = function (error) {
            return error;
        }

        this.get = function(url,parametros) {
            console.log(" AppServiceCaller -> url,parametros", url,parametros)
             console.log("-----------------------------------------------------")
             return $http.get(url, { params: parametros }, {});

        };
        this.post = function (url, parametros) {
            return $http.post(url, $httpParamSerializerJQLike(parametros), config).then(response, error);
        };
        this.put = function (url,parametros) {
            console.log("PUT AppServiceCaller -> url,parametros", url,parametros)
            return $http.put(url, $httpParamSerializerJQLike(parametros), config).then(response, error);
        };
        this.delete = function(url) {
            return $http.delete(url, { params: {} }, {}).then(response, error);
        };
         
});






