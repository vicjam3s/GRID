import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import "leaflet/dist/leaflet.css";
import "leaflet-defaulticon-compatibility";
import "leaflet-defaulticon-compatibility/dist/leaflet-defaulticon-compatibility.css";

const style = document.createElement("style");

style.innerHTML = `
.glass-card-hover {
  transition: all 0.35s ease;
}

.glass-card-hover:hover {
  transform: translateY(-6px) scale(1.01);
  box-shadow: 0 20px 40px rgba(0,0,0,0.2);
}

.program-card:hover {
  transform: translateY(-8px) scale(1.02);
  box-shadow: 0 22px 45px rgba(0,0,0,0.15);
}

@keyframes moveRoute {
  0% { transform: translateX(-100%) rotate(12deg); }
  100% { transform: translateX(100%) rotate(12deg); }
}

.program-button:hover {
  background: #ff846d;
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(0,0,0,0.15);
}

.subject-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 15px 35px rgba(0,0,0,0.12);
}

.back-button:hover {
  transform: translateX(-2px);
  box-shadow: 0 6px 16px rgba(0,0,0,0.15);
  background: rgba(255, 255, 255, 1) !important;
}

.topicItem:hover {
  background: #1E293B;
}

button:hover {
  background: #475569 !important;
}

`;

document.head.appendChild(style);
document.documentElement.style.scrollBehavior = "smooth";

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)