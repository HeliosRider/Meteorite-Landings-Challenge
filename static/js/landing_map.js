// Create the tile layer for the map background
let tileLayer = L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution: "&copy; <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors"
});
// Create the map object with initial settings
let map = L.map("map", {
    center: [37.0902, -95.7129],
    zoom: 5,
    layers: [tileLayer],
});
// Add the base tile layer to the map
tileLayer.addTo(map);
// Create the meteorite layer group
let meteorite = new L.LayerGroup();
// Base layers for the map
let baseMaps = {
    "OpenStreetMap": tileLayer,
};
// Overlay layer for the meteorites
let overlayMaps = {
    "Meteorites": meteorite,
};
// Add the layer control
L.control.layers(baseMaps, overlayMaps, { collapsed: false }).addTo(map);
// Fetch meteorite data
d3.json("http://127.0.0.1:5000/api/v1.0/meteorite-landings").then(function(data) {
    data.forEach(function(meteor) {
        console.log(meteor); // Check the structure of each meteorite object
        let geoLocation = meteor.GeoLocation.replace(/[()]/g, '').split(", ");
        let lat = parseFloat(geoLocation[0]);
        let lon = parseFloat(geoLocation[1]);
        // Create a marker for each meteorite
        let marker = L.marker([lat, lon]).addTo(meteorite);
        // Add a popup with the meteorite's name and year
        marker.bindPopup(`<b>Name:</b> ${meteor.name}<br><b>Year:</b> ${meteor.year}`);
    });
    // Add the meteorite layer to the map
    meteorite.addTo(map);
    
    legend.addTo(map);
});