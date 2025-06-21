function obj(p1, p2, p3) {
    this.p1=p1;
    this.p2=p2;
    this.p3=p3;
}

var x3=readLine();
var x = new obj(1, 2, 3);
var x2= new obj("ss", "$$", 435);
console.log(x2.p1, x2.p2, x2.p3);