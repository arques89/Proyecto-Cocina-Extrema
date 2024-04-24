export const Login = () => {
  return (
    <div>
        
        Login

        <form action="/dashboard" method="get">
            <label htmlFor="">Correo</label>
            <input type="email" name="email" id="" />            
            <label htmlFor="">Contraseña</label>
            <input type="password" name="password" id="" />
            <button type="submit">Entrar</button>
        </form>
    </div>

  )
}
