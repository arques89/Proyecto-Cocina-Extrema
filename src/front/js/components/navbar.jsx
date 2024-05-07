import { useContext } from "react";
import fondo from "../../img/LOGO_COCINA_EXTREMA.png";
import { Context } from "../store/appContext";
import { CDropdownMenu, CDropdownItem, CDropdownDivider, CDropdownToggle,CDropdown} from '@coreui/react';

export const NavBar = () => {
    const { actions, store } = useContext(Context);

    const handleLogout = () => {
        actions.logout(); // Llama a la acción de logout cuando se hace clic en el botón
    };

    return (
        <>
        <div className="navbar navbar-dark bg-dark nav-colored">
            <a href="/"><img className="navbar--logo" src={fondo} alt="" /></a>
            <p className="logo_title">Cocina Extrema</p>

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
                    </div>
                </li>
            </ul>

            <CDropdown dark>
                <CDropdownToggle color="secondary">

            <img height="70" width="70" src="http://www.gravatar.com/avatar/9017a5f22556ae0eb7fb0710711ec125?s=128" alt="Cloud Chen" style={{ borderRadius: "50%" }}/>
                </CDropdownToggle>
                    <CDropdownMenu >
                    <CDropdownItem href="#">Inicio / Registro</CDropdownItem>
                <CDropdownItem href="#">Perfil</CDropdownItem>
                <CDropdownItem href="#">Configuración</CDropdownItem>
                    <CDropdownDivider />
                    <CDropdownItem onClick={handleLogout}>Cerrar sesión</CDropdownItem>
                    </CDropdownMenu>
            </CDropdown>

        </div>
    </>
    );
};
