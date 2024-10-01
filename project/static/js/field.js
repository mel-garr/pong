
/* const gameStatuses = {
    START : 'StartGame',
    IN_PROGRESS: 'In'
}*/


export class Field{
    constructor (status ='StartGame', type, ballSide, maxScore =4, redteam, blueteam, width)
    {
        this.gametype = type; //for somebackend data m i want to store each type of game alone m i might have other types
        this.gameStatus = status; //game statue
        this.chosenBall = ballSide || 'red' ; //witch side will have ball at the start of the game or after every goal
        this.maxScore = maxScore; //max score to stop the game
        this.WinningTeam = 'none';


        this.redTeam = redteam || []; //a list of the object players
        this.redTeamScore = 0; //score of the team
        this.redTeamFsize = width/2; //to change later m it's the width where a player from red team can move
        //normally it's the half of the canvas but i want sometimes to be more depending on who the game is going
        this.redTeamFtype = 'none';


        this.blueTeam = blueteam || []; 
        this.blueTeamScore = 0;
        this.blueTeamFsize = width/2;
        this.blueTeamFtype = 'none';

    }
}