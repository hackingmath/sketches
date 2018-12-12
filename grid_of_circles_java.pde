void setup(){
    size(600,600);
    colorMode(HSB);
    rectMode(CENTER);
    noStroke();
}
    
int diam = 5; //diameter of each circle
    
void draw(){ //infinite loop
    translate(diam/2,diam/2);
    int num = width/diam;
    for (int j=0;j<num;j++){
        for (int i=0;i<num;i++){
            fill((4*frameCount+(i+j+5))%255,255,255);
            rect(i*diam,j*diam,diam,diam);
    }
    }
}
