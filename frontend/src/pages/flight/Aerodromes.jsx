import { Link } from "react-router-dom";

const aerodromes = [

  { icao: "HKJK", name: "Jomo Kenyatta International Airport", city: "Nairobi" },
  { icao: "HKMO", name: "Moi International Airport", city: "Mombasa" },
  { icao: "HKEL", name: "Eldoret International Airport", city: "Eldoret" },
  { icao: "HKNY", name: "Nanyuki Airport", city: "Nanyuki" },
  { icao: "HKLO", name: "Lokichoggio Airport", city: "Lokichoggio" }

];

export default function Aerodromes() {
  return (
    <div style={styles.page}>

      <Link to="/flight" style={styles.backButton} className="back-button">
        ← Back to Flight Planning
      </Link>

      <h1 style={styles.title}>Aerodrome Information</h1>

      <input
        placeholder="Search by ICAO or name"
        style={styles.search}
      />

      <div style={styles.grid}>

        {aerodromes.map((aero) => (

          <Link
            key={aero.icao}
            to={`/flight/aerodromes/${aero.icao}`}
            style={styles.card}
            className="aero-card"
          >

            <div style={styles.icao}>{aero.icao}</div>

            <div style={styles.name}>{aero.name}</div>

            <div style={styles.city}>{aero.city}</div>

          </Link>

        ))}

      </div>

    </div>
  );
}

const styles = {

  page: {
    minHeight: "100vh",
    padding: "80px 60px",
    fontFamily: "system-ui",
    background:
      "linear-gradient(135deg,#FFE4DE 0%, #FFD1C7 40%, #F4F4F4 100%)"
  },

  title: {
    fontSize: "42px",
    marginBottom: "30px"
  },

  search: {
    padding: "14px 18px",
    width: "100%",
    maxWidth: "500px",
    fontSize: "16px",
    borderRadius: "10px",
    border: "2px solid #FF9E8A",
    background: "rgba(255,255,255,0.9)",
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)",
    marginBottom: "40px",
    fontFamily: "system-ui",
    transition: "all 0.3s ease"
  },

  grid: {
    display: "grid",
    gridTemplateColumns: "repeat(3, 1fr)",
    gap: "25px",
    maxWidth: "1000px"
  },

  card: {
    padding: "24px",
    borderRadius: "14px",
    background: "rgba(255,255,255,0.65)",
    backdropFilter: "blur(10px)",
    textDecoration: "none",
    color: "#2E2E2E",
    boxShadow: "0 10px 25px rgba(0,0,0,0.08)",
    transition: "all 0.35s ease"
  },

  icao: {
    fontSize: "12px",
    fontWeight: "700",
    color: "#FF9E8A",
    marginBottom: "6px"
  },

  name: {
    fontSize: "18px",
    fontWeight: "500"
  },

  city: {
    fontSize: "14px",
    color: "#555"
  },

  backButton: {
    display: "inline-block",
    marginBottom: "40px",
    padding: "10px 20px",
    background: "rgba(255, 255, 255, 0.8)",
    color: "#2E2E2E",
    textDecoration: "none",
    borderRadius: "8px",
    fontWeight: "600",
    fontSize: "14px",
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)",
    transition: "all 0.3s ease",
    cursor: "pointer"
  }

};