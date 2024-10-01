export class Player{
    constructor(x = 30, y=10, width = 10, height = 30, ch, cw,goup = 'w', godown ='s', color='black'){
        this.x = x;
        this.y = y;
        // this.speed = speed;
        this.color = color;
        this.width = width;
        this.height = height;
        this.goup = goup;
        this.godown = godown;
        this.ch = ch
        this.cw = cw
        this.score = 0
        this.dy = 0;
        this.type = 'player';

        this.handleKeyDown = this.handleKeyDown.bind(this);
        this.handleKeyUp   = this.handleKeyUp.bind(this);

        document.addEventListener('keydown', this.handleKeyDown);
        document.addEventListener('keyup', this.handleKeyUp);

    }

    handleKeyDown(event){
        if (event.key.toLowerCase() == this.goup.toLowerCase())
            this.dy = -5;
        else if (event.key.toLowerCase() == this.godown.toLowerCase())
            this.dy = 5;
    }

    handleKeyUp(event){
        if (event.key.toLowerCase() == this.godown.toLowerCase() || event.key.toLowerCase() == this.goup.toLowerCase())
            this.dy = 0;
    }

    update(){
        if (this.dy < 0){
                this.y = Math.max(0, this.y + this.dy);
            }
            else
                this.y = Math.min(this.ch - this.height, this.y + this.dy);
    }

    reset(){
    }

    draw(ct){
		ct.fillStyle = this.color;
		ct.fillRect(this.x, this.y, this.width, this.height);
    }
}
