var scoreboardApp = angular.module('scoreboardApp', []);

scoreboardApp.controller('ScoreboardCtrl', function ($scope, $http) {
    $http({method: 'GET', url: '/api/teams'}).
    success(function(data, status, headers, config) {
        $scope.teams = data;
    }).
    error(function(data, status, headers, config) {
        alert("ERROR: " + data);
    });
});