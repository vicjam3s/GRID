import { Link } from "react-router-dom";

export default function Dashboard() {
  return (
    <div style={styles.page}>

      {/* Animated aviation background */}
      <div style={styles.routes}>
        <div style={styles.route}></div>
        <div style={styles.route2}></div>
        <div style={styles.route3}></div>
        <div style={styles.route4}></div>
        <div style={styles.route5}></div>
        <div style={styles.route6}></div>
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
          <div style={styles.glassCard} className="glass-card-hover">

            <h2 style={styles.panelTitle}>E-Learning</h2>

            <p style={styles.panelText}>
              Study aviation theory through structured modules covering
              navigation, meteorology, air law, aircraft performance and
              operational procedures. Practice exam questions and track
              your learning progress as you prepare for aviation exams.
            </p>

            <Link to="/learning">
              <button style={styles.button} className="program-button">
                Enter Learning
              </button>
            </Link>

          </div>
        </div>

        {/* FLIGHT PANEL */}
        <div style={{ ...styles.panel, ...styles.flight }}>
          <div style={styles.glassCard} className="glass-card-hover">

            <h2 style={styles.panelTitle}>Flight Planning</h2>

            <p style={styles.panelText}>
              Plan and manage flights using an interactive aviation map
              with aerodrome information, navigation tools and route
              building features. Monitor flights in real time and save
              routes for training or operational use.
            </p>

            <Link to="/flight">
              <button style={styles.buttonDark} className="program-button">
                Open Planner
              </button>
            </Link>

          </div>
        </div>

      </div>

      {/* GRID CAPABILITIES SECTION */}
<div style={styles.featuresSection}>

  <div style={styles.featuresContainer}>

    <h2 style={styles.featuresTitle}>GRID Capabilities</h2>

    <div style={styles.featuresGrid}>

      <div style={{...styles.featureCard, ...styles.cardLearning}} className="featureCard">
        <div style={styles.cardOverlay}>
          <h3 style={styles.featureTitle}>Structured Learning</h3>
          <p style={styles.featureText}>
            Aviation subjects organised into structured modules including
            navigation, meteorology, air law and aircraft performance.
          </p>
        </div>
      </div>

      <div style={{...styles.featureCard, ...styles.cardExams}} className="featureCard">
        <div style={styles.cardOverlay}>
          <h3 style={styles.featureTitle}>Practice Examinations</h3>
          <p style={styles.featureText}>
            Prepare for aviation exams using structured question banks
            designed to simulate real testing environments.
          </p>
        </div>
      </div>

      <div style={{...styles.featureCard, ...styles.cardPlanning}} className="featureCard">
        <div style={styles.cardOverlay}>
          <h3 style={styles.featureTitle}>Flight Route Planning</h3>
          <p style={styles.featureText}>
            Build and manage flight routes using an interactive aviation
            map with waypoint navigation tools.
          </p>
        </div>
      </div>

      <div style={{...styles.featureCard, ...styles.cardAerodrome}} className="featureCard">
        <div style={styles.cardOverlay}>
          <h3 style={styles.featureTitle}>Aerodrome Intelligence</h3>
          <p style={styles.featureText}>
            Access aerodrome information including frequencies,
            airspace structures and operational details.
          </p>
        </div>
      </div>

      <div style={{...styles.featureCard, ...styles.cardTracking}} className="featureCard">
        <div style={styles.cardOverlay}>
          <h3 style={styles.featureTitle}>Live Flight Tracking</h3>
          <p style={styles.featureText}>
            Monitor aircraft movements and follow flight paths in
            real time during navigation.
          </p>
        </div>
      </div>

      <div style={{...styles.featureCard, ...styles.cardNavigation}} className="featureCard">
        <div style={styles.cardOverlay}>
          <h3 style={styles.featureTitle}>Navigation Tools</h3>
          <p style={styles.featureText}>
            Advanced planning utilities including navigation logs,
            route building and situational awareness tools.
          </p>
        </div>
      </div>

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
    background: "#0F172A",
    position: "relative"
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
    color: "#F1F5F9",
    marginBottom: "10px",
    letterSpacing: "3px"
  },

  subtitle: {
    color: "#94A3B8",
    fontSize: "18px"
  },

  splitContainer: {
    display: "flex",
    minHeight: "380px",
    position: "relative",
    zIndex: 2
  },

  panel: {
    flex: 1,
    display: "flex",
    alignItems: "stretch",
    justifyContent: "center",
    padding: "30px",
  },

  // cleaner solid panels (no gradient noise)
  learning: {
  },

  flight: {
  },

  glassCard: {
    maxWidth: "520px",
    padding: "25px",
    borderRadius: "16px",
    background: "rgba(30,41,59,0.85)",
    backdropFilter: "blur(12px)",
    WebkitBackdropFilter: "blur(12px)",
    boxShadow: "0 12px 45px rgba(0,0,0,0.5)",
    color: "#F1F5F9",
    border: "1px solid #334155",
    display: "flex",
    flexDirection: "column",
    justifyContent: "space-between",
    flex: 1,
    transition: "all 0.35s ease",
    position: "relative",
    zIndex: 2
  },

  panelTitle: {
    fontSize: "32px",
    marginBottom: "12px"
  },

  panelText: {
    fontSize: "15px",
    lineHeight: "1.5",
    marginBottom: "15px",
    color: "#CBD5F5"
  },

  // unified grey buttons
  button: {
    padding: "12px 26px",
    borderRadius: "10px",
    border: "1px solid #475569",
    background: "#334155",
    color: "#F1F5F9",
    fontWeight: "600",
    cursor: "pointer",
    transition: "all 0.25s ease"
  },

  buttonDark: {
    padding: "12px 26px",
    borderRadius: "10px",
    border: "1px solid #475569",
    background: "#1E293B",
    color: "#F1F5F9",
    fontWeight: "600",
    transition: "all 0.25s ease",
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

  // softer, more realistic radar lines
  route: {
    position: "absolute",
    width: "120%",
    height: "2px",
    background: "rgba(255,255,255,0.08)",
    top: "40%",
    left: "-10%",
    transform: "rotate(12deg)",
    animation: "moveRoute 12s linear infinite"
  },

  route2: {
    position: "absolute",
    width: "120%",
    height: "2px",
    background: "rgba(255,255,255,0.05)",
    top: "65%",
    left: "-10%",
    transform: "rotate(-8deg)",
    animation: "moveRoute 18s linear infinite"
  },

  route3: {
    position: "absolute",
    width: "120%",
    height: "2px",
    background: "rgba(255,255,255,0.06)",
    top: "25%",
    left: "-10%",
    transform: "rotate(15deg)",
    animation: "moveRoute 15s linear infinite"
  },

  route4: {
    position: "absolute",
    width: "120%",
    height: "2px",
    background: "rgba(255,255,255,0.04)",
    top: "80%",
    left: "-10%",
    transform: "rotate(-12deg)",
    animation: "moveRoute 20s linear infinite"
  },

  route5: {
    position: "absolute",
    width: "120%",
    height: "2px",
    background: "rgba(255,255,255,0.07)",
    top: "50%",
    left: "-10%",
    transform: "rotate(8deg)",
    animation: "moveRoute 16s linear infinite"
  },

  route6: {
    position: "absolute",
    width: "120%",
    height: "2px",
    background: "rgba(255,255,255,0.05)",
    top: "35%",
    left: "-10%",
    transform: "rotate(-15deg)",
    animation: "moveRoute 22s linear infinite"
  },

  featuresSection: {
    padding: "100px 80px",
    textAlign: "center",
    position: "relative",
    zIndex: 2
  },

  featuresTitle: {
    fontSize: "42px",
    marginBottom: "60px",
    color: "#F1F5F9",
    fontWeight: "600"
  },

  featuresGrid: {
    display: "grid",
    gridTemplateColumns: "repeat(3, 1fr)",
    gap: "30px",
    justifyItems: "stretch",
    position: "relative",
    zIndex: 2
  },

  featureCard: {
    height: "220px",
    borderRadius: "16px",
    overflow: "hidden",
    position: "relative",
    zIndex: 2,
    backgroundSize: "cover",
    backgroundPosition: "center",
    cursor: "pointer",
    transition: "transform 0.35s ease, box-shadow 0.35s ease",
    boxShadow: "0 14px 40px rgba(0,0,0,0.5)"
  },

  featuresContainer: {
    maxWidth: "1200px",
    margin: "0 auto",
    position: "relative",
    zIndex: 1
  },

  // more subtle overlay (less contrast, more realism)
  cardOverlay: {
    position: "absolute",
    inset: 0,
    padding: "28px",
    background: "linear-gradient(rgba(15,23,42,0.55), rgba(15,23,42,0.95))",
    color: "white",
    display: "flex",
    flexDirection: "column",
    justifyContent: "flex-end",
    zIndex: 2
  },

  featureTitle: {
    fontSize: "20px",
    marginBottom: "8px"
  },

  featureText: {
    fontSize: "14px",
    lineHeight: "1.4",
    color: "#E2E8F0"
  },

};