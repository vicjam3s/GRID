import { Marker, Popup } from "react-leaflet";

const aerodromes = [
  {
    icao: "HKJK",
    name: "Jomo Kenyatta International",
    lat: -1.3192,
    lon: 36.9278,
  },
  {
    icao: "HKEL",
    name: "Eldoret Airport",
    lat: 0.4047,
    lon: 35.2389,
  },
  {
    icao: "HKMO",
    name: "Moi International",
    lat: -4.0348,
    lon: 39.5942,
  },
  {
    icao: "HKML",
    name: "Malindi Airport",
    lat: -3.2293,
    lon: 40.1017,
  },
];

export default function AerodromeLayer() {
  return (
    <>
      {aerodromes.map((aero) => (
        <Marker key={aero.icao} position={[aero.lat, aero.lon]}>
          <Popup>
            <b>{aero.icao}</b>
            <br />
            {aero.name}
          </Popup>
        </Marker>
      ))}
    </>
  );
}