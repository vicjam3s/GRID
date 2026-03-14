import { Polyline } from "react-leaflet";

const route = [
  [-1.3192, 36.9278], // HKJK
  [0.4047, 35.2389],  // HKEL
];

export default function RouteLayer() {
  return <Polyline positions={route} color="orange" />;
}