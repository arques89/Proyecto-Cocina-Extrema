import { useState } from 'react';
import { inputLogin } from "./mocks";
import config from '../../../config';
import { Navigate } from "react-router-dom";

export const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [token, setToken] = useState('');
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    if (name === 'email') setEmail(value);
    if (name === 'password') setPassword(value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    const formData = {
      email: email,
      password: password,
    };

    try {
      const response = await fetch(`${config.hostname}/login`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(formData)
      });

      if (!response.ok) {
        const responseData = await response.json();
        console.error(responseData.Error); // Maneja el error de alguna manera en tu aplicación
        return;
      }

      const responseData = await response.json();
      console.log("Inicio de sesión exitoso:", setToken(responseData));
      // Aquí podrías hacer algo con la respuesta del servidor, como redirigir al usuario a otra página.
    } catch (error) {
      console.error("Error al enviar formulario:", error);
    }
  };

  const renderInputLogin = () => {
    return inputLogin.map(item => (
      <div key={item.id}>
        <label htmlFor={item.htmlFor}>{item.label}</label><br />
        <input type={item.type} name={item.name} placeholder={item.placeholder} required onChange={handleInputChange} />
        <br />
      </div>
    ));
  };

  return (
    <>
    {token == null ? (
        <>
        <div className="container" id="login-container">
        <div className="content mt-5">
        <div className="login">
        <h2>Login</h2>
        <form onSubmit={handleSubmit}>
        {renderInputLogin()}
        <br />
        <button type="submit">Entrar</button>
        </form>
        </div>
        </div>
        </div>
        </>
    ) : (
        <Navigate to="/upFile" />
    )}
    </>
    );
};
