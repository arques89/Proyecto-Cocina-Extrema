import { BrowserRouter ,  Route } from 'react-router-dom';
import { Routes } from 'react-router-dom';

// import { NavBar } from './components/navbar';
// import { Footer } from './components/footer';
// import { Footer } from "./components/footer";

// import Home from "./pages/home";

// import "../styles/styles.css" 
// import "../styles/media.css" 
import { Chefs } from './pages/chefs';
import { Effect } from './pages/effect';
import { Formula } from './pages/formula';

const Layout = () => {
    return (
        <BrowserRouter>
            {/* <NavBar /> */}
            <Routes>
                {/* <Route path='/' Component={Home} /> */}
                <Route path='/chefs' Component={Chefs} />
                <Route path='/effect' Component={Effect} />
                <Route path='/' Component={Formula} />
            </Routes>
            {/* <Footer /> */}
        </BrowserRouter>
    )
}

export default Layout;