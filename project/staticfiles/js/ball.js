export class Ball{
    constructor(x = 30, y=10, ch, cw, radius = 10, speed=20, color='yellow', ){
        this.x = x;
        this.y = y;
        this.radius = radius;
        this.speed = speed;
        this.color = color;
        this.velocityX = Math.random() * 3 - 1;
        this.velocityY = (Math.random() * 3 - 1) < 0 ? -3 : 3;
        this.ch = ch;
        this.cw = cw;
        this.ls = 'none';//lastscore
        this.reset();
    }

    isCollidingWith(obj){
        // console.log ('ja hna');
        // top = obj.y;
        // bot = obj.y + obj.height;
        // left = obj.x;
        // right = obj.x +obj.width;
        return (
            this.x + this.radius > obj.x &&
            this.x - this.radius < obj.x + obj.width &&
            this.y + this.radius > obj.y &&
            this.y - this.radius < obj.y + obj.height
        );
    }
    
    handleCOllision(obj){
        console.log ('ja hnna')
        if (obj.type === 'player'){
            this.velocityX *= -1;
        }
    }

    update(objects = []){
        if (this.y + this.radius > this.ch || this.y - this.radius < 0){
            this.velocityY *= -1;
        }
        for (let obj of objects){
            if (this.isCollidingWith(obj)){
                this.handleCOllision(obj);
            }
        }
        if (this.x - this.radius < 0){
            this.ls = 'left';
            console.log(this.ls);
            this.reset();
        }
        else if (this.x + this.radius > this.cw){
            this.ls = 'right';
            console.log(this.ls);
            this.reset();
        }
        this.x += this.velocityX ;
        this.y += this.velocityY ;
    }

    reset(){
        this.x = this.cw/2 -2;
        this.y = this.ch/2 -2;
        this.velocityX = Math.random() * 3 - 1;
        this.velocityY = (Math.random() * 3 - 1) < 0 ? -3 : 3;
        // this.velocityX = 1;
        // this.velocityY = 0;
    }

    draw(ct){
        ct.beginPath();
		ct.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
		ct.fillStyle = this.color;
		ct.fill();
		ct.closePath();
    }
}

