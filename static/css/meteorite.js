console.log("Step 1")

//create tile layer for the map background
let tileLayer = L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution: "&copy; <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors",
  });

//create the map object with initial settings 
let map = L.map("map", {
    center: [37.0902, -95.7129],  // Starting position [latitude, longitude] (USA)
    zoom: 5,
    layers: [tileLayer],  // Adding the tile layer to the map
  });

//add the base tile layer to the map
tileLayer.addTo(map);

//create the meteorite layer
let meteorite = new L.LayerGroup();

//base layers for the map
let baseMaps = {
    "OpenStreetMap": tileLayer
};

//overlay layer for the meteorites
let overlayMaps = {
    "Meteorites": meteorite
}; 

//add the layer control 
L.control.layers(baseMaps, overlayMaps, {collapsed: false}).addTo(map);

//fetch meteorite data
// Using D3 to fetch and parse CSV data
d3.csv("static/resources/Meteorite_Data.csv").then(function(data) {
    console.log(data);
  }).catch(function(error) {
    console.error('Error loading the CSV file:', error);
  });
  

