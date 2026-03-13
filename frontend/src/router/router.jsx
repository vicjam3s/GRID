import { createBrowserRouter } from "react-router-dom";

import Home from "../pages/Home";

import Dashboard from "../pages/learning/Dashboard";
import Subjects from "../pages/learning/Subjects";
import Quiz from "../pages/learning/Quiz";

import FlightPlanner from "../pages/flight/FlightPlanner";

export const router = createBrowserRouter([
  {
    path: "/",
    element: <Home />,
  },

  {
    path: "/learning",
    element: <Dashboard />,
  },

  {
    path: "/learning/subjects",
    element: <Subjects />,
  },

  {
    path: "/learning/quiz",
    element: <Quiz />,
  },

  {
    path: "/flight",
    element: <FlightPlanner />,
  },
]);