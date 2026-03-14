import { Link } from "react-router-dom";

export default function LearningDashboard() {
  return (
    <div>
      <h1>Learning Dashboard</h1>

      <Link to="/learning/subjects">Subjects</Link>
      <br />
      <Link to="/learning/quiz">Practice Quiz</Link>
      <br />
      <Link to="/learning/exam">Exam Mode</Link>
    </div>
  );
}