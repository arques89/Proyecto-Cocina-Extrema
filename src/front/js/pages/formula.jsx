import config from "../../config";

export const Formula = () => {
  const handleSubmit = async (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    var headers = {}
    try {
      const response = await fetch(`${config.hostname}/crear_chef`, {
        method: 'POST',
        body: formData,
        'mode': 'cors',
        headers: headers,
        },
      );

      if (!response.ok) {
        throw new Error('Error al enviar el formulario');
      }

      console.log('Formulario enviado correctamente');
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <form action={`${config.hostname}/crear_chef`} method="post" encType="multipart/form-data" onSubmit={handleSubmit}>
      <ul>
        <li>
          <label htmlFor="name">Nombre:</label>
          <input type="text" id="name" name="name" />
        </li>
        <li>
          <label htmlFor="descripcion">Descripción:</label>
          <textarea id="descripcion" name="descripcion"></textarea>
        </li>
        <li>
          <label htmlFor="file">Subir Archivo:</label>
          <input type="file" name="imagen" id="imagen" />

        </li>
        <li>
          <button type="submit">Guardar</button>
        </li>
      </ul>
    </form>
  );
};
