$vpd=4;
pi=3.14;
innerH=3;   innerR=4;
outerH=3.5; outerR=6.75;
dik=.1;
hoek=60;
module ring(h, r)
{
  difference() {
    cylinder(h=h, r=r+dik);
    translate([0,0,-5])
      cylinder(h=h+10, r=r); // negative object higher
  }
}

module muur(hoek) {
  rotate([0,0,hoek])
    translate([innerR,0,0])
      cube([outerR-innerR, dik, innerH]);
}

module biogas()
{
  scale(v=[.1,.1,.1]) {
    union() {
      ring(innerH, innerR);
      ring(outerH, outerR);
      muur(0);
      muur(hoek);
    }
  }
}
biogas();
function betonRing (dia, dik) = let(r=dia+dik) (r*r - dia*dia) * pi * innerH;
function betonMuur() = 2 * dik * innerH * (outerR-innerR);
function inner3(r, h, hoek) = h * hoek / 360 * r * r * pi;
function ring3(angle) = inner3(outerR, innerH, angle) - inner3(innerR+dik, innerH, angle);

e="euro";
baksteen=.23;
gasbetonM3 = 0.6*0.4*0.05;
steenM2 = 78*.21*.05;
specieM2 = dik*(1-steenM2)*1.5;
murenM3=betonMuur();
ringM3=betonRing(innerR, dik);
beton=murenM3+ringM3;
aantalM2=beton/dik;
aantalBakstenen=beton/dik*78; //stenenPerM2=78
echo(murenM3=betonMuur());
echo(ringM3=betonRing(innerR, dik));
echo(innerM3=inner3(innerR, innerH, 360));
echo(plugflowM3=ring3(360-hoek));
echo(effluentM3=ring3(hoek));
echo(beton=beton, prijs=120*beton);
echo(gasbetonM3=gasbetonM3, prijs=1.8*beton/gasbetonM3);
echo(perM2=78*baksteen, aantalM2=aantalM2, stuks=aantalBakstenen);
echo(steenM2=steenM2, specieM2=specieM2);
baksteenKosten=aantalBakstenen*baksteen;
specieKosten=specieM2*aantalM2/12*3.9*1000;
echo(allesM2=baksteenKosten, specie=specieKosten);
echo(materiaalKosten=specieKosten+baksteenKosten);
echo(serreMuurPerM2=1700, e);
echo(totalM3=inner3(outerR, innerH, 360));
echo(betonplaten=100/2.40/1.20*2);
echo("https://www.123betonbestellen.nl/berekenen");

