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
    padding: "25px",
    borderRadius: "16px",
    background: "rgba(255,255,255,0.25)",
    backdropFilter: "blur(12px)",
    WebkitBackdropFilter: "blur(12px)",
    boxShadow: "0 8px 30px rgba(0,0,0,0.15)",
    color: "white",
    display: "flex",
    flexDirection: "column",
    justifyContent: "space-between",
    flex: 1,
    transition: "all 0.35s ease"
  },

  panelTitle: {
    fontSize: "32px",
    marginBottom: "12px"
  },

  panelText: {
    fontSize: "15px",
    lineHeight: "1.5",
    marginBottom: "15px"
  },

  button: {
    padding: "12px 26px",
    borderRadius: "10px",
    border: "none",
    background: "white",
    color: "#FF8A73",
    fontWeight: "600",
    cursor: "pointer",
    transition: "all 0.3s ease"
  },

  buttonDark: {
    padding: "12px 26px",
    borderRadius: "10px",
    border: "none",
    background: "#FF9E8A",
    color: "white",
    fontWeight: "600",
    transition: "all 0.3s ease",
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
  padding: "100px 80px",
  textAlign: "center"
},

featuresTitle: {
  fontSize: "42px",
  marginBottom: "60px",
  color: "#2E2E2E",
  fontWeight: "600"
},

featuresGrid: {
  display: "grid",
  gridTemplateColumns: "repeat(3, 1fr)",
  gap: "30px",
  justifyItems: "stretch"
},

featureCard: {
  height: "220px",
  borderRadius: "16px",
  overflow: "hidden",
  position: "relative",
  backgroundSize: "cover",
  backgroundPosition: "center",
  cursor: "pointer",
  transition: "transform 0.35s ease, box-shadow 0.35s ease",
  boxShadow: "0 10px 30px rgba(0,0,0,0.15)"
},

featuresContainer: {
  maxWidth: "1200px",
  margin: "0 auto"
},

cardOverlay: {
  position: "absolute",
  inset: 0,
  padding: "28px",
  background: "linear-gradient(rgba(0,0,0,0.45), rgba(0,0,0,0.7))",
  color: "white",
  display: "flex",
  flexDirection: "column",
  justifyContent: "flex-end"
},

featureTitle: {
  fontSize: "20px",
  marginBottom: "8px"
},

featureText: {
  fontSize: "14px",
  lineHeight: "1.4"
},

cardLearning: {
  backgroundImage:
    "url('https://images.unsplash.com/photo-1457369804613-52c61a468e7d')"
},

cardExams: {
  backgroundImage:
    "url('https://images.unsplash.com/photo-1503676260728-1c00da094a0b')"
},

cardPlanning: {
  backgroundImage:
    "url('https://images.unsplash.com/photo-1529070538774-1843cb3265df')"
},

cardAerodrome: {
  backgroundImage:
    "url('https://images.unsplash.com/photo-1508444845599-5c89863b1c44')"
},

cardTracking: {
  backgroundImage:
    "url('https://images.unsplash.com/photo-1474302770737-173ee21bab63')"
},

cardNavigation: {
  backgroundImage:
    "url('https://images.unsplash.com/photo-1500530855697-b586d89ba3ee')"
},

};