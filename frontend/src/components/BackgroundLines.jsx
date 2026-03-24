export default function BackgroundLines() {
  return (
    <div style={styles.routes}>
      <div style={styles.route}></div>
      <div style={styles.route2}></div>
      <div style={styles.route3}></div>
      <div style={styles.route4}></div>
      <div style={styles.route5}></div>
      <div style={styles.route6}></div>
    </div>
  );
}

const styles = {
  routes: {
    position: "absolute",
    width: "100%",
    height: "100%",
    top: 0,
    left: 0,
    zIndex: 1,
    overflow: "hidden",
    pointerEvents: "none"
  },

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
  }
};
