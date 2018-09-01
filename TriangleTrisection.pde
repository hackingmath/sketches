/* Copying keith_briain's Instagram post
Trisecting an Equilateral Triangle
Sept. 1, 2018 */

float sz = 280; //"radius" of triangle
PVector O,A,B,C,D,E,F,G,H,I,J,K,L,M,N,P,Q,R,S;
PShape hex;

void setup(){
  size(600,600);
}

void draw(){
  background(0);
  stroke(0,255,0);
  translate(width/2,height/2);
  //Vertices of Triangle
  O = new PVector(0,0); //Center of triangle
  A = new PVector(O.x+sz*cos(radians(-90)),O.y+sz*sin(radians(-90)));
  B = new PVector(O.x+sz*cos(radians(-210)),O.y+sz*sin(radians(-210)));
  C = new PVector(O.x+sz*cos(radians(-330)),O.y+sz*sin(radians(-330)));
  
  strokeWeight(2);
  line(A.x,A.y,B.x,B.y);
  line(A.x,A.y,C.x,C.y);
  line(C.x,C.y,B.x,B.y);
  
  //Midpoints of sides of triangle
  D = new PVector((A.x+C.x)/2,(A.y+C.y)/2);
  //float Dy = (A.y+C.y)/2;
  E = new PVector((A.x+B.x)/2,(A.y+B.y)/2);
  F = new PVector((B.x+C.x)/2,(B.y+C.y)/2);
  
  strokeWeight(1);
  line(D.x,D.y,E.x,E.y);
  line(E.x,E.y,F.x,F.y);
  line(D.x,D.y,F.x,F.y);
  
    //Trisecting points of sides of triangle
  G = new PVector((2*A.x+C.x)/3,(2*A.y+C.y)/3);
  H = new PVector((A.x+2*C.x)/(3),(A.y+2*C.y)/(3));
  I = new PVector((2*A.x+B.x)/3,(2*A.y+B.y)/3);
  J = new PVector((A.x+2*B.x)/(3),(A.y+2*B.y)/(3));
  K = new PVector((2*B.x+C.x)/3,(2*B.y+C.y)/3);
  L = new PVector((B.x+2*C.x)/(3),(B.y+2*C.y)/(3));
 
  strokeWeight(1);
  line(B.x,B.y,G.x,G.y);
  line(B.x,B.y,H.x,H.y);
  line(C.x,C.y,I.x,I.y);
  line(C.x,C.y,J.x,J.y);
  line(A.x,A.y,K.x,K.y);
  line(A.x,A.y,L.x,L.y);
  
  //ELLIPSE
  noFill();
  stroke(255,255,0);
  ellipse(O.x,O.y,sz,sz);
  
  //Small Hexagon
  M = new PVector((2*D.x+E.x)/3,(2*D.y+E.y)/3);
  N = new PVector((D.x+2*E.x)/(3),(D.y+2*E.y)/(3));
  P = new PVector((2*F.x+E.x)/3,(2*F.y+E.y)/3);
  Q = new PVector((F.x+2*E.x)/(3),(F.y+2*E.y)/(3));
  R = new PVector((2*D.x+F.x)/3,(2*D.y+F.y)/3);
  S = new PVector((D.x+2*F.x)/(3),(D.y+2*F.y)/(3));
  
  stroke(255,0,255);
  hex = createShape();
  hex.beginShape();
  hex.fill(255,0,255,50);
  hex.vertex(M.x,M.y);
  hex.vertex(N.x,N.y);
  hex.vertex(Q.x,Q.y);
  hex.vertex(P.x,P.y);
  hex.vertex(S.x,S.y);
  hex.vertex(R.x,R.y);
  hex.endShape(CLOSE);
  
  shape(hex,0,0);
  /*
  strokeWeight(3);
  stroke(255,0,0);
  line(M.x,M.y,N.x,N.y);
  line(Q.x,Q.y,N.x,N.y);
  line(P.x,P.y,Q.x,Q.y);
  line(P.x,P.y,S.x,S.y);
  line(R.x,R.y,S.x,S.y);
  line(M.x,M.y,R.x,R.y);
  */
  scale(1.732);
  strokeWeight(2);
  stroke(255,0,0);
  line(M.x,M.y,N.x,N.y);
  line(Q.x,Q.y,N.x,N.y);
  line(P.x,P.y,Q.x,Q.y);
  line(P.x,P.y,S.x,S.y);
  line(R.x,R.y,S.x,S.y);
  line(M.x,M.y,R.x,R.y);
  
}
