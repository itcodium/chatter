
var ModalTemplate = function () {
    this.modal_name = ""
    this.title = ""
    this.text = ""
    this.app_text = ""
    // this.model = {}
    this.items = {}
    this.method="";
    this.click = function () {
        console.log("Click this.modal_name", this.modal_name);
    },
    this.show = function () {
        $("#" + this.modal_name).modal('show');
    }
    this.hide = function (form) {   
        JSArrays.deleteFromArray(this.items, this.key_id, this.model[this.key_id])
        if (typeof this.form != 'undefined') { 
            this.form.$setPristine();
            this.form.$setUntouched();
        }
        $("#" + this.modal_name).modal('hide');
        this.resetModel();
    }
    this.resetModel = function () {
        this.select_index = -1;
        this.model_aux = {};
        this.model = {};
    }
    this.cancel = function () {
        this.items[this.select_index] = angular.copy(this.model_aux)
        this.resetModel();
    }
    this.open = function (method, index) {
        this.method=method;
        if (method == API_METHOD.EDIT){
            this.title=this.pageText.editTitle;
        }
        if (method == API_METHOD.DELETE){
            this.title=this.pageText.deleteTitle;
        }
        if (method == API_METHOD.ADD){
            this.title=this.pageText.addTitle;
        }
        if (method == API_METHOD.EDIT || method == API_METHOD.DELETE) {
            if (typeof index !== 'undefined') {
                this.setItem(index)
            }
        }
        // else {this.resetModel();}
        this.method = method;
        this.show();
    }

    this.setItems = function (data) {
        this.items = data;
    }
    this.setItem = function (index) {
        this.select_index = index;
        this.model_aux = angular.copy(this.items[index]);
        this.model = this.items[index]
        
    }
}
