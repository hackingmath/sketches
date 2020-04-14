/* Copy of Atticus Bones design
need p5.js file to work
Makes one eigth of the design,
then reflects and rotates to fill the grid.
But the rotation is a little off in CodePen.
June 30, 2017 */

var sz = 5; //distance between dots
var nodes = ['blank']; //list of nodes
var mirrornodes = ['blank']; //list of reflected nodes
var connections = [
    [1,2],[1,4],
    [2,3],[2,4],[2,5],
    [3,5],[3,7],
    [4,5],[4,6],
    [5,6],[5,7],
    [6,7],[6,8],
    [7,8],[7,9],
    [8,9]];

var g;
var gridList = []; //list for grids

function setup(){
  createCanvas(600,600); // window size
  for (var i = 0; i < 484; i++){
   gridList.push(new Grid());
  }
  // for (var i=0;i<10;i++){
  //   console.log(int(random(2)));
  // }
  //g = new Grid();
}

function draw(){
  background (255); //white
  //translate(width/2,height/2);

  fill(0); //black dots
  //loop through rows
  for (var x=0;x<22; x++){
    for (var y=0; y<22; y++){
    push();//save this location
    translate(6*x*sz,6*y*sz);
     gridList[22*x+y].display()
    //g.display();
    pop();//return to saved location
}
}
}

function Node(x,y,num){
  //Node Object has its own properties
  this.x = x;
  this.y = y;
  this.num = num;
  
  this.display = function(){
    //this is how to display it
    fill(0);
    ellipse(this.x,this.y,10,10);
  }
  
  this.connect = function(other){
    strokeWeight(1);
    //stroke(0,255,0);
    line(this.x,this.y,
        other.x,other.y);
  }
}

function Grid(){
  //create the nodes in the grid
  nodes.push(new Node(0,0,1))
  nodes.push(new Node(0,-sz,2)); //node 1
  nodes.push(new Node(0,-2*sz,3)); //node 2
  nodes.push(new Node(sz/2.0,-sz/2.0,4)); //node 3
  nodes.push(new Node(0.5*sz,-1.5*sz,5)); //node 4
  nodes.push(new Node(sz,-sz,6)); //node 5
  nodes.push(new Node(sz,-2*sz,7)); //node 6
  nodes.push(new Node(1.5*sz,-1.5*sz,8)); //node 7
  nodes.push(new Node(2*sz,-2*sz,9)); //node 8
  
  //create the reflected nodes in the grid
  mirrornodes.push(new Node(0,0,1))
  mirrornodes.push(new Node(sz,0,2)); //node 1
  mirrornodes.push(new Node(2*sz,0,3)); //node 2
  mirrornodes.push(new Node(sz/2,-sz/2,4)); //node 3
  mirrornodes.push(new Node(1.5*sz,-0.5*sz,5)); //node 4
  mirrornodes.push(new Node(sz,-sz,6)); //node 5
  mirrornodes.push(new Node(2.0*sz,-sz,7)); //node 6
  mirrornodes.push(new Node(1.5*sz,-1.5*sz,8)); //node 7
  mirrornodes.push(new Node(2.0*sz,-2*sz,9)); //node 8
  
  //each grid gets its own color:
  this.col = 0;
  //Uncomment to make it colorful
  //this.col = color(random(255),random(255), random(255));
  //list of connections
  var connectChoice = [];
  //fill the list with random 0's and 1's
  for (var i=0; i<16; i++){
    connectChoice.push(int(random(2)));
  }
  
  this.connect = function(){
    for (var i=0; i<connectChoice.length; i++){
      var c = connectChoice[i];
      if (c == 1){
        nodes[connections[i][0]].connect(nodes[connections[i][1]]);
        mirrornodes[connections[i][0]].connect(mirrornodes[connections[i][1]]);
      }
    }
  }
  
  this.display = function(){
      for(var i=0; i<4; i++){
        rotate(i*radians(90));
        stroke(this.col);
        this.connect(); //grid connects
        }
      
    }
  }
