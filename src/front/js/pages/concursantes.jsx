import { useEffect, useState } from "react";
import { CardPerson } from "../components/cardPerson"
import config from "../../config";

export const Concursantes = () => {

  const [users, setUsers] = useState([]);

  useEffect(() => {

    fetch(`${config.hostname}/concursantes`, {
      method: "GET",
    })
      .then((data) => data.json())
      .then(json => setUsers(json))
      .catch((error) => {
        error;
      });
  }, []);
  return (
    <div className="container" id="card-container">
      <h1>Concursantes</h1>
      <div className="row row-cols-1 row-cols-md-3 g-4">
        {users.map(user => (
          <div key={user.id} className="col">
            <CardPerson
              imageConcursantes={user.image}
              concursantesName={user.name}
              concursantesDescription={user.description}
            />
          </div>
        ))}
      </div>
    </div>
  )
}