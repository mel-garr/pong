export class Field{
    constructor (redTeam, blueteam, maxScore = 5)
    {
        this.redTeam = redTeam;
        this.blueteam = blueteam;
        this.redScore = 0;
        this.blueScore = 0;
        this.maxScore = maxScore;
        this.redFieldType = 'default';
        this.blueFieldType = 'default';
    }

    increaseScore(team){
        if (team === 'blue'){
            this.blueScore++;
        } else if (team === 'red'){
            this.redScore++;
        }
    }

    isGameOver(){
        return this.redScore >= this.maxScore || this.blueScore >= this.maxScore;
    }

    getWinner(){
        if (this.blueScoreScore >= this.maxScore){
            return 'blue';
        } else if (this.redScoreScore >= this.maxScore){
            return 'red';
        }
        return null;
    }
}