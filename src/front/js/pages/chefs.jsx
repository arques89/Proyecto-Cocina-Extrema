import { useEffect, useState } from "react";
import { CardPerson } from "../components/cardPerson"
import config from "../../config";

export const Chefs = () => {

    const [users, setUsers] = useState([]);

    useEffect(() => {
  
      fetch(`${config.hostname}/chefs`, {
        method: "GET",
      })
        .then((data) => data.json())
        .then(json => setUsers(json))
        .catch((error) => {
          error;
        });
    }, []);
    return (

        <>
        {users.map(user => (
            <>
            <div key={user.id} className="container text-dark">
                <CardPerson
                    
                    imageChef={user.image}
                    chefName={user.name}
                    chefDescription={user.description}
                />
            </div>
            </>
             ))}
             </>
    )
}