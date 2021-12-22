import React, {useState, useEffect} from "react";
import './App.css';

function App() {

  const BASE_URL = "http://localhost:3000/"

  const [posts, setPosts] = useState([]);

  useEffect(() => {
    fetch(BASE_URL + "post/all")
  }, [])

  return (
    "Hello, World!"
  );
}

export default App;
