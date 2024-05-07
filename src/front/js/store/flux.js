// import { genConfig } from "react-nice-avatar";
import config from "../../config";
import toast from "react-hot-toast";

const getState = ({ getStore, getActions, setStore }) => {
  return {
    store: {
      token: null,
      avatar: null,

      demo: [
        {
          title: "FIRST",
          background: "white",
          initial: "white",
        },
        {
          title: "SECOND",
          background: "white",
          initial: "white",
        },
      ],
    },
    actions: {
      register: async (email, password, name, surname) => {
        try {
          const response = await fetch(`${config.hostname}/register`, {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({ email, password, name, surname }),
          });
          if (!response.ok) {
			// console.log(response)
            const responseData = await response.json();
            const notify = () => toast.error(`${responseData.error}`);

            throw new Error(notify());
          }

          // Generar la configuración del Avatar con el valor de email del formulario
          return toast.success("Registro satisfactorio, por favor revise su bandeja de entrada"), 201;
          // Añadir la configuración del avatar al estado avatar del store Flux
        } catch (error) {
          return; // Retorna temprano en caso de error
        }
      },

      login: async (email, password) => {
        try {
          const response = await fetch(`${config.hostname}/login`, {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({ email, password }),
          });

          if (!response.ok) {
            const responseData = await response.json();
            const notify = () => toast.error(responseData.error);
            throw new Error(notify());
          }

          const responseData = await response.json();
          setStore({ token: responseData.token }); // Almacena el token en el estado global
        } catch (error) {
          console.error("Error al iniciar sesión:", error);
        }
      },

      logout: () => {
        // Eliminar el token
        setStore({ token: null });
        // Redirigir al usuario a la página de inicio de sesión
        window.location.href = "/login";
      },

      // Use getActions to call a function within a fuction
      exampleFunction: () => {
        getActions().changeColor(0, "green");
      },
      loadSomeData: () => {
        /**
					fetch().then().then(data => setStore({ "foo": data.bar }))
				*/
      },
      changeColor: (index, color) => {
        //get the store
        const store = getStore();

        //we have to loop the entire demo array to look for the respective index
        //and change its color
        const demo = store.demo.map((elm, i) => {
          if (i === index) elm.background = color;
          return elm;
        });

        //reset the global store
        setStore({ demo: demo });
      },
    },
  };
};

export default getState;
