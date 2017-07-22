import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './pages/App';
import LiveMatch from './pages/LiveMatch';
import SummonerStats from './pages/SummonerStats';
import About from './pages/About';
import registerServiceWorker from './registerServiceWorker';
import { Route, HashRouter, Switch } from 'react-router-dom';
import SiteNav from "./components/Nav"

const app = document.getElementById('root');

const Main = () => (
  <main>
    <Switch>
      <Route exact path="/" component={App}></Route>
      <Route path="/stats" component={SummonerStats}></Route>
      <Route path="/live" component={LiveMatch}></Route>
      <Route path="/about" component={About}></Route>
    </Switch>
  </main>
)

// The Header creates links that can be used to navigate
// between routes.
const Header = () => (
  <header>
    <SiteNav />
  </header>
)

const Routing = () => (
  <div>
    <Header />
    <Main />
  </div>
)

// This demo uses a HashRouter instead of BrowserRouter
// because there is no server to match URLs
ReactDOM.render((
  <HashRouter>
    <Routing />
  </HashRouter>
), app)