import config from "../../config";
import bcrypt from "bcryptjs";

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
    const hashedPassword = await bcrypt.hash(password, 10);

    // Crear el objeto formData con la contraseña hasheada
    const formData = {
      name: name,
      surname: surname,
      email: email,
      password: hashedPassword
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
        throw new Error("Error al enviar el formulario");
      }

      console.log("Formulario enviado correctamente");
      // Aquí podrías hacer algo con la respuesta del servidor, como redirigir al usuario a otra página.
    } catch (error) {
      console.error("Error al enviar el formulario:", error);
      return; // Retorna temprano en caso de error
    }
  };

  return (
    <div>
      <h2>Registro</h2>
      <form onSubmit={handleSubmit}>
        <label htmlFor="name">Nombre</label>
        <input type="text" name="name" id="name" required />
        <br />
        <label htmlFor="surname">Apellido</label>
        <input type="text" name="surname" id="surname" required />
        <br />
        <label htmlFor="email">Correo</label>
        <input type="email" name="email" id="email" required />
        <br />
        <label htmlFor="password">Contraseña</label>
        <input type="password" name="password" id="password" required />
        <br />
        <button type="submit">Registrarse</button>
      </form>
    </div>
  );
};
