import { useState, StrictMode, lazy, Suspense } from "react";
import { render } from "react-dom";
import { Route, Switch, Link } from "react-router-dom";
import ThemeContext from "./ThemeContext";

const Details = lazy(() => import("./Details"));
const SearchParams = lazy(() => import("./SearchParams"));

const App = () => {
  const theme = useState("darkblue");
  return (
    <StrictMode>
      <ThemeContext.Provider value={theme}>
        <div>
          <h2>This h2 will not go away</h2>
          <Suspense fallback={<h2>is loading</h2>}>
            <Router>
              <header>
                <Link to="/">Adopt Me!</Link>
              </header>
              <Switch>
                <Route path="/details/:id">
                  <Details />
                </Route>
                <Route path="/">
                  <SearchParams />
                </Route>
              </Switch>
            </Router>
          </Suspense>
        </div>
      </ThemeContext.Provider>
    </StrictMode> 
  );
};

render(
  <StrictMode>
    <App />
  </StrictMode>,
  document.getElementById("root")
);
