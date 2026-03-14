import { Link } from "react-router-dom";

export default function Dashboard() {
  return (
    <div style={styles.page}>

      <div style={styles.header}>
        <h1 style={styles.title}>GRID</h1>
        <p style={styles.subtitle}>
          Aviation Learning & Flight Planning Platform
        </p>
      </div>

      <div style={styles.splitContainer}>

        <Link to="/learning" style={{ ...styles.panel, ...styles.learning }}>
          <div>
            <h2>E-Learning</h2>
            <p>Study aviation theory and prepare for exams</p>
          </div>
        </Link>

        <Link to="/flight" style={{ ...styles.panel, ...styles.flight }}>
          <div>
            <h2>Flight Planning</h2>
            <p>Plan routes and navigate with aviation maps</p>
          </div>
        </Link>

      </div>

    </div>
  );
}

const styles = {

  page: {
    height: "100vh",
    display: "flex",
    flexDirection: "column",
    background: "#F4F4F4",
  },

  header: {
    textAlign: "center",
    padding: "40px 0",
  },

  title: {
    fontSize: "48px",
    color: "#2E2E2E",
    marginBottom: "10px",
  },

  subtitle: {
    color: "#555",
  },

  splitContainer: {
    flex: 1,
    display: "flex",
  },

  panel: {
    flex: 1,
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    textDecoration: "none",
    color: "white",
    fontSize: "22px",
    transition: "all 0.3s ease",
  },

  learning: {
    background: "#FF9E8A",
  },

  flight: {
    background: "#2E2E2E",
  },
};