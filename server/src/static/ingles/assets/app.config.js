 

// Configuración de las rutas
app.config(function ($routeProvider) {

    $routeProvider
        .when('/', {
            templateUrl: 'assets/pages/categories/list.html',
            controller: 'controllerCategoriesList'
        })
         .when('', {
             templateUrl: 'assets/pages/index.html#/categories/list',
             controller: 'controllerCategoriesList'
         })
        .when('/categories/list', {
            templateUrl: 'assets/pages/categories/list.html',
            controller: 'controllerCategoriesList'
        })
        .when('/phrases/list', {
            templateUrl: 'assets/pages/phrases/list.html',
            controller: 'controllerPhrasesList'
            
        })
        .otherwise({
            redirectTo: '/'
        });
});

