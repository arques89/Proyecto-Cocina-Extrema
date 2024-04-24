import { BrowserRouter ,  Route } from 'react-router-dom';
import { Routes } from 'react-router-dom';

import { NavBar } from './components/navbar';
// import { Footer } from './components/footer';
import { Footer } from "./components/footer";

import Home from "./pages/home";

import "../styles/styles.css" 
import "../styles/media.css" 
import { Chefs } from './pages/chefs';
// import { Effect } from './pages/effect';
import { Formula } from './pages/formula';
import { Concursantes } from './pages/concursantes';
import { Login } from './pages/login';
import { Register } from './pages/register';

const Layout = () => {
    return (
        <BrowserRouter>
            <NavBar />
            <Routes>
                <Route path='/' Component={Home} />
                <Route path='/login' Component={Login} />
                <Route path='/register' Component={Register} />
                <Route path='/chefs' Component={Chefs} />
                <Route path='/concursantes' Component={Concursantes} />
                {/* <Route path='/effect' Component={Effect} /> */}
                <Route path='/form' Component={Formula} />
            </Routes>
            <Footer />
        </BrowserRouter>
    )
}

export default Layout;