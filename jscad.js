function main() {
  return [
    rotate_extrude(
      {fn:1},   // aantal facetten, minimaal 8
      square({size:[.03,3.5]}) // te extruderen oppervlak
        .translate([6.75,0,0]) // grootte van de cirkel
    )
  ];
}
