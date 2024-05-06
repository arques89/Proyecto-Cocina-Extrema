import config from "../../../config";
import bcrypt from "bcryptjs";
import toast, { Toaster } from 'react-hot-toast';

import { inputRegister } from './mocks' 

export const Register = () => {
  

  const handleSubmit = async (event) => {
    event.preventDefault();

    // Verificar si el formulario es válido antes de enviar la solicitud
    if (!event.target.checkValidity()) {
      console.error("El formulario es inválido");
      return;
    }

    // Obtener los valores del formulario
    const name = event.target.elements.name.value;
    const surname = event.target.elements.surname.value;
    const email = event.target.elements.email.value;
    const password = event.target.elements.password.value;

    // Verificar si los campos están vacíos
    if (!name || !surname || !email || !password) {
      console.error("Por favor, completa todos los campos");
      return;
    }

    // Hashear la contraseña antes de enviarla al servidor
    // const hashedPassword = await bcrypt.hash(password, 10);

    // Crear el objeto formData con la contraseña hasheada
    const formData = {
      name: name,
      surname: surname,
      email: email,
      password: password
    };

    try {
      const response = await fetch(`${config.hostname}/register`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(formData)
      });

      if (!response.ok) {
        const responseData = await response.json();
        const notify = () => toast.error(`${responseData.message}`);

        throw new Error(notify());
      }
      
      console.log("Formulario enviado correctamente");
      // Aquí podrías hacer algo con la respuesta del servidor, como redirigir al usuario a otra página.
    } catch (error) {
      return; // Retorna temprano en caso de error
    }
  };

  const renderInputRegister = () => {
    return inputRegister.map(item => (
      <div key={item.id}>
      <label htmlFor={item.htmlFor}>{item.label}</label><br />
      <input type={item.type} name={item.name} placeholder={item.placeholder} required />
      <br />
      </div>
    ))
  }

  return (
    <div className="container" id="register-container">
        <div className="content mt-5">
            <div className="register">
                <h2>Registro</h2>
                <form onSubmit={handleSubmit}>
                    {renderInputRegister()}
                    <br />
                    <button type="submit">Registrarse</button>
                </form>
            </div>
            <Toaster
            position="top-center"
            reverseOrder={false}
            />
        </div>
    </div>
  );
};
