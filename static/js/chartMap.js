$.ajax({
    url: "http://algebrawinteriotkceple.westeurope.cloudapp.azure.com:80/api/telemetry/devices",
    data: {
    },
    cache: false,
    type: "GET",
    success: function(response) {
        devids = [];
        names = [];
        lats = [];
        longs = [];

        console.log(response)

        for(var i = 0; i < response.length; i++) {
            devids[i] = response[i][0];
            names[i] = response[i][1];
            lats[i] = parseFloat(response[i][2]);
            longs[i] = parseFloat(response[i][3]);
        }

        var map = L.map('Mymap').setView([45.2705, 45.1500], 3);

        L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
        }).addTo(map);

        for(var i = 0; i < response.length; i++) {
            L.marker([lats[i], longs[i]])
                .bindPopup('<a href="' + devids[i] + '" target="_blank">' + names[i] + '</a>')
                .addTo(map);
        }
    },
    error: function(xhr) {
        console.log("Ajax error!");
        console.log(xhr);
    }
})