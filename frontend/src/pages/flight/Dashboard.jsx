import { Link } from "react-router-dom";

export default function FlightDashboard() {
  return (
    <div>
      <h1>Flight Planning</h1>

      <Link to="/flight/planner">Open Flight Planner</Link>
    </div>
  );
}