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
    padding: "12px",
    width: "300px",
    borderRadius: "8px",
    border: "1px solid #ddd",
    marginBottom: "40px"
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
  }

};