import { useState, useContext } from "react";
import { Context } from "../../store/appContext"; // Importa el contexto
import { inputLogin } from "./mocks";
import { Navigate } from "react-router-dom";
import  { Toaster } from 'react-hot-toast';

export const Login = () => {
  const { actions, store } = useContext(Context); // Obtén las acciones y el estado del contexto

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    if (name === "email") setEmail(value);
    if (name === "password") setPassword(value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    actions.login(email, password); // Llama a la acción de inicio de sesión
  };

  const renderInputLogin = () => {
    return inputLogin.map((item) => (
      <div key={item.id}>
        <label htmlFor={item.htmlFor}>{item.label}</label>
        <br />
        <input
          type={item.type}
          name={item.name}
          placeholder={item.placeholder}
          required
          onChange={handleInputChange}
        />
        <br />
      </div>
    ));
  };

  return (
    <>
      {store.token === null ? (
        <div className="login-container">
          <div className="video-login">
            <video className="video" loop autoPlay muted>
              <source
                src="https://res.cloudinary.com/dztgp8g6w/video/upload/v1714975087/6822612-hd_1080_2048_25fps_dp32fa.mp4"
                type="video/mp4"
              />
            </video>
          </div>
          <div className="login-form">
            <div className="content mt-5">
                <h2>Login</h2>
              <div className="login">
                <form onSubmit={handleSubmit}>
                  {renderInputLogin()}
                  <br />
                  <button type="submit">Entrar</button>
                </form>
              </div>
              <Toaster
            position="top-center"
            reverseOrder={false}
            />
            </div>
          </div>
        </div>
      ) : (
        <Navigate to="/dashboard" />
      )}
    </>
  );
};
