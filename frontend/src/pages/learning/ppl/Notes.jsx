import BackgroundLines from "../../../components/BackgroundLines";

export default function Notes() {
  return (
    <div style={styles.page}>
      <BackgroundLines />
      <div style={styles.content}>
        <h1>Subject Notes</h1>
      </div>
    </div>
  );
}

const styles = {
  page: {
    minHeight: "100vh",
    padding: "60px",
    fontFamily: "system-ui",
    background: "#0F172A",
    position: "relative"
  },
  content: {
    position: "relative",
    zIndex: 2
  }
};