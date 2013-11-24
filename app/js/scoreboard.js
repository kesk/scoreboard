var scoreboardApp = angular.module('scoreboardApp', []);

scoreboardApp.controller('ScoreboardCtrl', function ($scope) {
	$scope.teams = ['Team 1', 'Team 2'];
});