import { MapContainer, TileLayer, Marker, Popup, Polyline } from "react-leaflet";
import { useNavigate } from "react-router-dom";
import "leaflet/dist/leaflet.css";

import L from "leaflet";
import markerIcon from "leaflet/dist/images/marker-icon.png";
import markerShadow from "leaflet/dist/images/marker-shadow.png";

delete L.Icon.Default.prototype._getIconUrl;

L.Icon.Default.mergeOptions({
  iconUrl: markerIcon,
  shadowUrl: markerShadow,
});

const aerodromes = [

  { icao: "HKJK", name: "Jomo Kenyatta Intl", position: [-1.3192, 36.9278] },
  { icao: "HKMO", name: "Moi Intl Airport", position: [-4.0348, 39.5942] },
  { icao: "HKEL", name: "Eldoret Intl Airport", position: [0.4045, 35.2389] },
  { icao: "HKNY", name: "Nanyuki Airport", position: [0.0624, 37.0383] },
  { icao: "HKLO", name: "Lokichoggio Airport", position: [4.2041, 34.3482] }

];

export default function MapView({ departure, destination }) {

  const navigate = useNavigate();

  const dep = aerodromes.find(a => a.icao === departure);
  const dest = aerodromes.find(a => a.icao === destination);

  const route =
    dep && dest ? [dep.position, dest.position] : null;

  return (

    <MapContainer
      center={[-0.0236, 37.9062]}
      zoom={6}
      style={{ height: "100%", width: "100%", borderRadius: "14px" }}
    >

      <TileLayer
        attribution="© OpenStreetMap contributors"
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />

      {aerodromes.map((aero) => (

        <Marker key={aero.icao} position={aero.position}>

          <Popup>

            <strong>{aero.icao}</strong>
            <br />
            {aero.name}

            <br /><br />

            <button
              onClick={() => navigate(`/flight/aerodromes/${aero.icao}`)}
              style={{
                padding: "6px 10px",
                borderRadius: "6px",
                border: "none",
                background: "#FF9E8A",
                color: "white",
                cursor: "pointer"
              }}
            >
              View Aerodrome
            </button>

          </Popup>

        </Marker>

      ))}

      {route && (
        <Polyline
          positions={route}
          pathOptions={{ color: "#FF5733", weight: 4 }}
        />
      )}

    </MapContainer>

  );
}