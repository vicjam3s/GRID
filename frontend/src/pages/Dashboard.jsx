import { Link } from "react-router-dom";

export default function Dashboard() {
  return (
    <div style={{ padding: 40 }}>
      <h1>GRID</h1>

      <div style={{ display: "flex", gap: 40 }}>
        <Link to="/learning">
          <button>E-Learning</button>
        </Link>

        <Link to="/flight">
          <button>Flight Planning</button>
        </Link>
      </div>
    </div>
  );
}