import { Link } from "react-router-dom";

export default function Dashboard() {
  return (
    <div style={styles.page}>

      {/* Animated aviation background */}
      <div style={styles.routes}>
        <div style={styles.route}></div>
        <div style={styles.route2}></div>
      </div>

      <div style={styles.header}>
        <h1 style={styles.title}>GRID</h1>
        <p style={styles.subtitle}>
          Aviation Learning & Flight Planning Platform
        </p>
      </div>

      <div style={styles.splitContainer}>

        {/* LEARNING PANEL */}
        <div style={{ ...styles.panel, ...styles.learning }}>
          <div style={styles.glassCard}>

            <h2 style={styles.panelTitle}>E-Learning</h2>

            <p style={styles.panelText}>
              Study aviation theory through structured modules covering
              navigation, meteorology, air law, aircraft performance and
              operational procedures. Practice exam questions and track
              your learning progress as you prepare for aviation exams.
            </p>

            <Link to="/learning">
              <button style={styles.button}>
                Enter Learning
              </button>
            </Link>

          </div>
        </div>

        {/* FLIGHT PANEL */}
        <div style={{ ...styles.panel, ...styles.flight }}>
          <div style={styles.glassCard}>

            <h2 style={styles.panelTitle}>Flight Planning</h2>

            <p style={styles.panelText}>
              Plan and manage flights using an interactive aviation map
              with aerodrome information, navigation tools and route
              building features. Monitor flights in real time and save
              routes for training or operational use.
            </p>

            <Link to="/flight">
              <button style={styles.buttonDark}>
                Open Planner
              </button>
            </Link>

          </div>
        </div>

      </div>

      {/* GRID CAPABILITIES SECTION */}
      <div style={styles.featuresSection}>

        <h2 style={styles.featuresTitle}>GRID Capabilities</h2>

        <div style={styles.featuresGrid}>

          <div style={styles.featureCard}>
            <h3>Structured Learning</h3>
            <p>
              Aviation subjects organised into clear modules including
              navigation, meteorology, air law and aircraft performance.
            </p>
          </div>

          <div style={styles.featureCard}>
            <h3>Practice Examinations</h3>
            <p>
              Prepare for aviation exams using structured question banks
              designed to simulate real test environments.
            </p>
          </div>

          <div style={styles.featureCard}>
            <h3>Flight Route Planning</h3>
            <p>
              Build and manage flight routes with an interactive aviation
              map and waypoint navigation tools.
            </p>
          </div>

          <div style={styles.featureCard}>
            <h3>Aerodrome Intelligence</h3>
            <p>
              Access detailed aerodrome information including frequencies,
              airspace structures and operational data.
            </p>
          </div>

          <div style={styles.featureCard}>
            <h3>Live Flight Tracking</h3>
            <p>
              Monitor aircraft movements and follow flight paths in real
              time during navigation.
            </p>
          </div>

          <div style={styles.featureCard}>
            <h3>Navigation Tools</h3>
            <p>
              Advanced planning utilities for route building, navigation
              logs and situational awareness during flight operations.
            </p>
          </div>

        </div>

      </div>

    </div>
  );
}

const styles = {

  page: {
    minHeight: "100vh",
    display: "flex",
    flexDirection: "column",
    fontFamily: "system-ui",
    paddingBottom: "80px",
    background:
      "linear-gradient(135deg,#FFE4DE 0%, #FFD1C7 40%, #F4F4F4 100%)",
  },

  header: {
    textAlign: "center",
    paddingTop: "60px",
    paddingBottom: "40px",
    position: "relative",
    zIndex: 2
  },

  title: {
    fontSize: "80px",
    fontWeight: "700",
    color: "#2E2E2E",
    marginBottom: "10px",
    letterSpacing: "3px"
  },

  subtitle: {
    color: "#555",
    fontSize: "18px"
  },

  splitContainer: {
    display: "flex",
    minHeight: "520px",
    position: "relative",
    zIndex: 2
  },

  panel: {
    flex: 1,
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    padding: "40px",
  },

  learning: {
    background:
      "linear-gradient(135deg,#FF9E8A 40%, #ffb7a5ef 100%)"
  },

  flight: {
    background:
      "linear-gradient(135deg,#2E2E2E 0%, #3a3a3ae9 100%)"
  },

  glassCard: {
    maxWidth: "420px",
    padding: "35px",
    borderRadius: "16px",
    background: "rgba(255,255,255,0.25)",
    backdropFilter: "blur(12px)",
    WebkitBackdropFilter: "blur(12px)",
    boxShadow: "0 8px 30px rgba(0,0,0,0.15)",
    color: "white"
  },

  panelTitle: {
    fontSize: "36px",
    marginBottom: "20px"
  },

  panelText: {
    fontSize: "16px",
    lineHeight: "1.6",
    marginBottom: "25px"
  },

  button: {
    padding: "12px 26px",
    borderRadius: "10px",
    border: "none",
    background: "white",
    color: "#FF8A73",
    fontWeight: "600",
    cursor: "pointer"
  },

  buttonDark: {
    padding: "12px 26px",
    borderRadius: "10px",
    border: "none",
    background: "#FF9E8A",
    color: "white",
    fontWeight: "600",
    cursor: "pointer"
  },

  routes: {
    position: "absolute",
    width: "100%",
    height: "100%",
    top: 0,
    left: 0,
    zIndex: 1,
    overflow: "hidden"
  },

  route: {
    position: "absolute",
    width: "120%",
    height: "2px",
    background: "rgba(255,255,255,0.3)",
    top: "40%",
    left: "-10%",
    transform: "rotate(12deg)",
    animation: "moveRoute 12s linear infinite"
  },

  route2: {
    position: "absolute",
    width: "120%",
    height: "2px",
    background: "rgba(255,255,255,0.2)",
    top: "65%",
    left: "-10%",
    transform: "rotate(-8deg)",
    animation: "moveRoute 18s linear infinite"
  },

  featuresSection: {
    padding: "80px 60px",
    textAlign: "center"
  },

  featuresTitle: {
    fontSize: "40px",
    marginBottom: "50px",
    color: "#2E2E2E"
  },

  featuresGrid: {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fit, minmax(260px, 1fr))",
    gap: "30px"
  },

  featureCard: {
    padding: "25px",
    borderRadius: "14px",
    background: "rgba(255,255,255,0.35)",
    backdropFilter: "blur(10px)",
    boxShadow: "0 6px 18px rgba(0,0,0,0.08)",
    textAlign: "left"
  }

};