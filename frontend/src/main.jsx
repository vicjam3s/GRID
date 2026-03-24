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

.subject-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 15px 35px rgba(0,0,0,0.12);
}

.back-button,
.primary-button,
.secondary-button {
  transition: all 0.25s ease;
}

.back-button:hover,
.primary-button:hover,
.secondary-button:hover {
  background: rgba(51, 65, 85, 0.9) !important;
  border-color: #475569 !important;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.7);
  transform: translateY(-2px);
}

.back-button:active,
.primary-button:active,
.secondary-button:active {
  transform: translateY(0);
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