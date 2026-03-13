import { useEffect, useState } from "react";
import API from "../../api/api";

export default function Subjects() {
  const [subjects, setSubjects] = useState([]);

  useEffect(() => {
    API.get("subjects/").then((res) => {
      setSubjects(res.data);
    });
  }, []);

  return (
    <div>
      <h1>Subjects</h1>

      {subjects.map((s) => (
        <div key={s.id}>{s.name}</div>
      ))}
    </div>
  );
}