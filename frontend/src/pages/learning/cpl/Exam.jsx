import BackgroundLines from "../../../components/BackgroundLines";

export default function Exam() {
  return (
    <div style={styles.page}>
      <BackgroundLines />
      <div style={styles.content}>
        <h1>Exam Mode</h1>
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