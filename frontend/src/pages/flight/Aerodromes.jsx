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
    background: "#0F172A"
  },

  title: {
    fontSize: "42px",
    marginBottom: "30px",
    color: "#F1F5F9"
  },

  // dark command-style search bar
  search: {
    padding: "14px 18px",
    width: "100%",
    maxWidth: "500px",
    fontSize: "16px",
    borderRadius: "10px",
    border: "1px solid #334155",
    background: "#020617",
    color: "#F1F5F9",
    boxShadow: "0 6px 20px rgba(0,0,0,0.5)",
    marginBottom: "40px",
    fontFamily: "system-ui",
    outline: "none",
    transition: "all 0.25s ease"
  },

  grid: {
    display: "grid",
    gridTemplateColumns: "repeat(3, 1fr)",
    gap: "25px",
    maxWidth: "1000px"
  },

  // aerodrome cards (database entries)
  card: {
    padding: "24px",
    borderRadius: "14px",
    background: "rgba(30,41,59,0.9)",
    backdropFilter: "blur(10px)",
    textDecoration: "none",
    color: "#F1F5F9",
    border: "1px solid #334155",
    boxShadow: "0 12px 40px rgba(0,0,0,0.6)",
    transition: "all 0.3s ease"
  },

  // ICAO codes styled like identifiers
  icao: {
    fontSize: "12px",
    fontWeight: "700",
    color: "#94A3B8",
    marginBottom: "6px",
    letterSpacing: "1px"
  },

  name: {
    fontSize: "18px",
    fontWeight: "500"
  },

  city: {
    fontSize: "14px",
    color: "#CBD5F5"
  },

  backButton: {
    display: "inline-block",
    marginBottom: "40px",
    padding: "10px 20px",
    background: "rgba(30,41,59,0.9)",
    color: "#F1F5F9",
    textDecoration: "none",
    borderRadius: "8px",
    fontWeight: "600",
    fontSize: "14px",
    border: "1px solid #334155",
    boxShadow: "0 6px 20px rgba(0,0,0,0.5)",
    transition: "all 0.25s ease",
    cursor: "pointer"
  }

};