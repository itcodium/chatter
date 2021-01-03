 
var CategoriesModule = (function () {
    var PageText = {
        "category": "Categoria",
        "description": "Descripcion",
        "addTitle":"Agregar Categoria",
        "editTitle":"Editar Categoria",
        "deleteTitle":"Borrar Categoria"
    };

    
    var validate = new FormValidations();
    
    function CategoriesBase($scope, AppServiceCaller, AplicationText) {
        $scope.pageText = PageText;
        $scope.AplicationText = AplicationText;
        $scope.api = new ApiCaller();
        $scope.api.setRoute("categories");
        $scope.api.setCaller(AppServiceCaller);
    };

    this.CategoriesList = function ($scope, $route,$filter,$route, AppServiceCaller, AplicationText) {
        CategoriesBase.call(this, $scope, AppServiceCaller, AplicationText);
        

        $scope.title = "Listado de categorias"
        $scope.modalEdit = new ModalTemplate();
        $scope.modalEdit.setItems($scope.models);
        
        $scope.modalEdit.modal_name = "editCategories";
        $scope.modalEdit.key_id = "_id";
        $scope.modalEdit.template = { src: "assets/pages/categories/categories.html" };
        $scope.modalEdit.pageText = $scope.pageText;
        $scope.modalEdit.AplicationText = AplicationText;

        $scope.modalEdit.submit = function (form) {
            this.form = form;
            if (form.$valid) {
                if (this.method == "EDIT") {
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
        $scope.api.get();
 
    };

 
    return {
        CategoriesListController: this.CategoriesList
    };

})();

                
app.controller('controllerCategoriesList', ["$scope", "$route", "$filter","$route", "AppServiceCaller", "AplicationText", CategoriesModule.CategoriesListController])



 


