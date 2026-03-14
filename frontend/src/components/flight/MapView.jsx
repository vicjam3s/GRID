import { MapContainer, TileLayer } from "react-leaflet";
import AerodromeLayer from "./AerodromeLayer";

export default function MapView() {
  return (
    <MapContainer
      center={[-1.286389, 36.817223]} // Nairobi
      zoom={7}
      style={{ height: "100vh", width: "100%" }}
    >
      <TileLayer
        attribution="OpenStreetMap"
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />

      <AerodromeLayer />
    </MapContainer>
  );
}