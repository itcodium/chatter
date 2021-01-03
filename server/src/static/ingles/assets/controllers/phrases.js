 
var PhrasesModule = (function () {
    _this=this;
    var PageText = {
        "category" : "Categoria",
        "us" : "US",
        "es" : "ES",
        "meaning" : "Significado",
        "addTitle":"Agregar texto",
        "editTitle":"Editar texto",
        "deleteTitle":"Borrar texto",
        "emptyList":"No se encontraron registros."
    };

    
    var validate = new FormValidations();
    
    var apiCategories =new  ApiCaller();


    function PhrasesBase($scope, AppServiceCaller, AplicationText) {
        $scope.pageText = PageText;
        $scope.AplicationText = AplicationText;
        
        $scope.api = new ApiCaller();
        $scope.api.setRoute("phrases");
        $scope.api.setCaller(AppServiceCaller);

        apiCategories.setRoute("categories");
        apiCategories.setCaller(AppServiceCaller)
    };
    
    
        

    this.PhrasesList = function ($scope, $route,$filter,$location,$route, AppServiceCaller, AplicationText) {
        
        PhrasesBase.call(this, $scope, AppServiceCaller, AplicationText);
        

        $scope.title = "Listado de phrases"
        $scope.modalEdit = new ModalTemplate();
        $scope.modalEdit.setItems($scope.models);

        
        $scope.modalEdit.modal_name = "editPhrases";
        $scope.modalEdit.key_id = "_id";
        $scope.modalEdit.template = { src: "assets/pages/phrases/phrases.html" };
        $scope.modalEdit.pageText = $scope.pageText;
        $scope.modalEdit.AplicationText = AplicationText;
 
        $scope.modalEdit.category=$location.search();
        $scope.modalEdit.model={};
        $scope.modalEdit.model.category=$location.search().category;
        //$scope.modalEdit.categories=JSON.parse(localStorage.getItem("categories"));
        $scope.modalEdit.submit = function (form) {
            this.form = form;
            if (form.$valid) {
                if (this.method == "EDIT") {
                    $scope.api.apiName="phrases";
                    $scope.api.put($scope.modalEdit.model._id.$oid, $scope.modalEdit.model);
                }
                if (this.method == "DELETE") {
                    $scope.api.delete($scope.modalEdit.model._id.$oid);
                }
                if (this.method == "ADD") {
                    $scope.modalEdit.model.creado_por="test"
                    $scope.api.post($scope.modalEdit.model);
                }
            }
        }
     
        $scope.api.setScope($scope);
        $scope.api.get($location.search(),Get_callBack);

        function Get_callBack(res) {
            $scope.modalEdit.items = res.data;
            apiCategories.get({},$scope.GetCategorias_callBack);
        }

        $scope.GetCategorias_callBack= function(res) {
            $scope.modalEdit.categories = res.data;
        }
            
    };
    return {
        PhrasesListController: this.PhrasesList
    };

})();


app.controller('controllerPhrasesList', ["$scope", "$route", "$filter","$location","$route", "AppServiceCaller", "AplicationText", PhrasesModule.PhrasesListController])
 