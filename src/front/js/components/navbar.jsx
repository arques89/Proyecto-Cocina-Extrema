import React, { useState } from 'react';
import fondo from "../../img/LOGO_COCINA_EXTREMA.png";

import { Login } from '../pages/login';
import { Register } from '../pages/register';
import { Menu } from './menu';

export const NavBar = () => {

    const [showLogin, setShowLogin] = useState(false);
    const [showRegister, setShowRegister] = useState(false);

    const toggleLogin = () => {
        setShowLogin(!showLogin);
    };
    const toggleRegister = () => {
        setShowRegister(!showRegister);
    };

    return (
        <>
        {/* // <!-- Header --> */}
        <div className="navbar navbar-dark bg-dark nav-colored">
            {/* <!-- Logotipo --> */}
            <a href="/"><img className="navbar--logo" src={fondo} alt="" /></a>
            <p className="logo_title">Cocina Extrema</p>

            {/* <!-- Menú hamburgueza --> */}

            <ul className="navbar-nav ml-auto">
                <li className="nav-item">
                    <button
                        className="navbar-toggler"
                        type="button"
                        data-toggle="collapse"
                        data-target="#navbarToggleExternalContent"
                        aria-controls="navbarToggleExternalContent"
                        aria-expanded="false"
                        aria-label="Toggle navigation"
                    >
                        <span className="navbar-toggler-icon"></span>
                    </button>
                    <div
                        className="dropdown-menu dropdown-menu-right"
                        aria-labelledby="navbarDropdown"
                        id="navbarToggleExternalContent"
                    >

                        <a className="dropdown-item" href="/">PROGRAMAS</a>
                        <a className="dropdown-item" href="/">RECETAS</a>
                        <a className="dropdown-item" href="/">CONCURSANTES</a>
                        <a className="dropdown-item" href="/">COCINEROS</a>
                        {/* <button onClick={acceso()} >Login</button>
                    <button value={false}>Register</button> */}
                        {/* <button className='btn btn-dark mx-3' onClick={toggleLogin}>{!showLogin ? 'Login' : 'Menu'}</button>
                        {showLogin ? <Login /> : <Menu />} */}

                        {/* <button className='btn btn-dark mx-3' onClick={toggleRegister}>{!showRegister ? 'Register' : 'Menu'}</button>
                        {showRegister ? <Register /> : <Menu />} */}



                    </div>
                </li>
            </ul>



           
                <button className="btn circle my-auto" type="button" id="dropdownMenuButton2" data-bs-toggle="dropdown" aria-expanded="false">

                        <img height="70" width="70" src="http://www.gravatar.com/avatar/9017a5f22556ae0eb7fb0710711ec125?s=128" alt="Cloud Chen"/>

                    
                </button>
                <ul className="dropdown-menu dropdown-menu-dark dropdown-menu-end">
                    <li><button className="dropdown-item" type="button">Inicio / Registro</button></li>
                    <li><button className="dropdown-item" type="button">Perfil</button></li>
                    <li><button className="dropdown-item" type="button">Configuración</button></li>
                    <li><hr className="dropdown-divider" /></li>
                    <li><button className="dropdown-item" type="button">Cerrar sesión</button></li>
                </ul>
        


        </div>
    </>
    );
};