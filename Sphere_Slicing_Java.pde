float diam = 250;
float t = 0;
int centerx = 0;
int centery = 0;
float centerz = -1.5*diam;
float d,diam_slice,h;

void setup() {
  size(600, 600,P3D);
  background(0);
  rectMode(CENTER);
  
  colorMode(HSB);
  noFill();
  strokeWeight(2);
}

void draw() {
  background(0);
  translate(200,300,-100);
  float rot = -map(mouseX,0,width,0,TWO_PI);
  float tilt = -map(mouseY,0,width,0,TWO_PI);
  rotateX(tilt);//radians(30));
  rotateY(rot);//-PI/4);
  
  for (int i=-150;i<150;i+=20){
    //First the squares
    stroke(255);
    rect(0,0,300,300);
    //This wave thing doesn't work for this!
    //var d = 300 + diam*sin(t + i/10.0);
    //It's really just the distance from the 
    //center of the circle
    d = dist(0,0,i,centerx,centery,centerz);
    diam_slice = 2*sqrt(pow((diam/2.0),2)-pow(d,2));
    h = map(i,-150,150,0,300);
    stroke(h,255,255);
    ellipse(0,0, diam_slice,diam_slice);
    translate(0,0,20);
  }
  centerz += t;
  t += 0.01;
  if (centerz > 1.5*diam){
    t = 0.0;
    centerz = -1.5*diam;
  }
  /*if (frameCount % 3 == 0){
    saveFrame("####.png");
  }*/
}
