$vpd=4;
pi=3.14;
effR=4;
inH=3;    inR=3;
outH=3.5; outR=6.75;
schaal=0.05;
module ring(h, r, dik)
{
  difference() {
    cylinder(h=h, r=r+dik);
    translate([0,0,-5])
      cylinder(h=h+10, r=r); // negative object higher
  }
}

module biogas()
{
  scale(v=[schaal,schaal,schaal]) {
    union() {
      ring(outH, outR, 0.4);
      difference() {
        translate([7,0,0])
          ring(outH, effR, 0.1);
        translate([0,0,-5])
          ring(outH+10, outR, 20);
      }
    }
  }
}
biogas();

echo("https://www.hmg-benelux-shop.com/hmg_h/polyester-golfplaat-op-rol-7618-080-mm-naturel-95elpe7618r.html");
