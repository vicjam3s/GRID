import { useParams } from "react-router-dom";

export default function SubjectDetail() {
  const { id } = useParams();

  return (
    <div>
      <h1>Subject {id}</h1>
    </div>
  );
}