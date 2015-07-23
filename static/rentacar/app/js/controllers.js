'use strict';

/* Controllers */
var rentaCarApp = angular.module('RentaCarApp', ['daterangepicker']);

rentaCarApp.controller('TabController', function($scope) {
    $scope.tab = 1;
    $scope.selectTab = function (setTab){
        $scope.tab = setTab;
    };
    $scope.isSelected = function(checkTab) {
        return $scope.tab === checkTab;
    };
  });

rentaCarApp.controller('CarAvailController', ['$scope', '$http', function($scope, $http) {
    $http.get('http://127.0.0.1:8000/carrental/avail_cars/').success(function(data) {
    $scope.cars = data
  });
  }]);

rentaCarApp.controller('CheckCarAvailController', ['$scope', '$http', function($scope, $http) {
    $scope.availCars = [];
    $scope.formOK = false;
    $scope.form = {};
    $scope.date = {startDate: null, endDate: null};
    $scope.form.carId = null;

    $http.get('http://127.0.0.1:8000/carrental/avail_cars/').success(function(data) {
        $scope.cars = data;
  });
  $scope.form.submitForm = function(item, event) {
    console.log("--> submitting form");
    console.log($scope.form.carId);
    var startDate = $scope.date.startDate.format('YYYY-MM-DD hh:mm:ss[+00:00]');
    var endDate = $scope.date.endDate.format('YYYY-MM-DD hh:mm:ss[+00:00]');
    console.log(startDate);
    var dataObject = {
        car_id : $scope.form.carId,
        start: startDate,
        end: endDate
    };   
    //TODO change to post
    var responsePromise;
    if(dataObject.car_id != null && dataObject.car_id != "null" )
        responsePromise = $http.get("http://127.0.0.1:8000/carrental/avail_cars/"+dataObject.car_id+"/"+
            dataObject.start + "/" + dataObject.end + "/");
    else 
        responsePromise = $http.get("http://127.0.0.1:8000/carrental/avail_cars/"+
                    dataObject.start + "/" + dataObject.end + "/");

    responsePromise.success(function(dataFromServer, status, headers, config){
       console.log(dataFromServer); 
       $scope.availCars = dataFromServer;
       $scope.formOK = true;
    });
  };
    
  }]);
rentaCarApp.controller('RentaCarController', ['$scope', '$http', function($scope, $http) {
    $scope.formOK = false;
    $scope.form = {};
    $scope.date = {startDate: null, endDate: null};
    $scope.form.carId = null;

    $http.get('http://127.0.0.1:8000/carrental/avail_cars/').success(function(data) {
        $scope.cars = data;
  });
  $scope.form.submitForm = function(item, event) {
    console.log("--> submitting form");
    console.log($scope.form.carId);
    var startDate = $scope.date.startDate.format('YYYY-MM-DD hh:mm:ss[+00:00]');
    var endDate = $scope.date.endDate.format('YYYY-MM-DD hh:mm:ss[+00:00]');
    console.log(startDate);
    var dataObject = {
        car_id : $scope.form.carId,
        start: startDate,
        end: endDate
    };   
    //TODO change to post
    var responsePromise = $http.get("http://127.0.0.1:8000/carrental/rent_car/"+dataObject.car_id+"/"+
        dataObject.start + "/" + dataObject.end + "/");

    responsePromise.success(function(dataFromServer, status, headers, config){
       console.log(dataFromServer); 
       $scope.formOK = true;
    });
  };
    
  }]);
