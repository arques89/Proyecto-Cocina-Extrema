import { useState } from 'react';
import PropTypes from 'prop-types';
import { Modal } from "../components/modal";

export const CardPerson = ({ imageChef, chefName , chefDescription }) => {
    const [showModal, setShowModal] = useState(false);

    const handleOpenModal = () => {
        setShowModal(true);
    };

    const handleCloseModal = () => {
        setShowModal(false);
    };

    CardPerson.propTypes = {
        imageChef: PropTypes.string.isRequired,
        chefName: PropTypes.string.isRequired,
        chefDescription: PropTypes.string.isRequired,
      };

    return (
        <>
            <div className="row row-cols-1 row-cols-md-3 g-4 my-5">
                <div className="col">
                    <div className="card">
                        <img src={imageChef} className="card-img-top" alt={chefName} />
                        <div className="card-body">
                            <h5 className="card-title">{chefName}</h5>
                            <p className="card-text">{chefDescription}</p>
                            <button className="btn btn-primary" onClick={handleOpenModal}>Saber más</button>
                        </div>
                    </div>
                </div>
            </div>
            {showModal && <Modal onClose={handleCloseModal} chefName={"Martin Berasategui"} />}
        </>
    );
};

