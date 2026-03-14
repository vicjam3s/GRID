import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import "leaflet/dist/leaflet.css";
import "leaflet-defaulticon-compatibility";
import "leaflet-defaulticon-compatibility/dist/leaflet-defaulticon-compatibility.css";

const style = document.createElement("style");

style.innerHTML = `
.featureCard:hover {
  transform: translateY(-10px);
  box-shadow: 0 20px 45px rgba(0,0,0,0.25);
}
`;


document.head.appendChild(style);

style.innerHTML = `
@keyframes moveRoute {
  0% { transform: translateX(-100%) rotate(12deg); }
  100% { transform: translateX(100%) rotate(12deg); }
}
`;



document.head.appendChild(style);
document.documentElement.style.scrollBehavior = "smooth";

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
