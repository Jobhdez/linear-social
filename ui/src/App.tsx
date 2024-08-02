import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";
import InputExpression from "./components/InputExpression";

function App() {
  const [count, setCount] = useState(0);

  return <InputExpression />;
}

export default App;
