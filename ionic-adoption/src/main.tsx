import React from "react";
import { createRoot } from "react-dom/client";
import App from "./App";

const container = document.getElementById("root");
const root = createRoot(container!);
root.render(
    // I may re-enable strict mode later.
    // <React.StrictMode>
    <App />
    // </React.StrictMode>
);
