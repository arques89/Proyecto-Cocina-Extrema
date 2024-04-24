import Plaqueta from "../../img/ROJO_VIDEO.png"
import Sombrero from "../../img/ROJO_sombrero-de-cocinero.png"
import Bandeja from "../../img/ROJO_bandeja.png"

import { Slider } from "../components/slider";
import { Video } from "../components/video";
import { Card } from "../components/card";

import image from "../../img/masterchef-celebrity-8.jpg";
import image2 from "../../img/pexels-sebastian.jpg";
import image3 from "../../img/final-masterchef.jpg";
import image4 from "../../img/finalistas.jpg";

import video1 from "../../img/canal-cocina-portada-1100x619.jpg"
import video2 from "../../img/pexels-sebastian-coman.jpg";

import sponsor from "../../img/bosch.png";
import sponsor1 from "../../img/elcorteingles.png";
import sponsor2 from "../../img/arcos.png";
import sponsor3 from "../../img/lecreuset.png";
import sponsor4 from "../../img/aeg.png";

const Home = () => {
    return (
        <main>
            <Slider />
            
            {/* <!-- Contenido principal --> */}

            <div className="container">
                <div id="texto-img" className="row mb-5 icons">
                    {/* <!-- Primera columna de imagen --> */}
                    <div className="col text-center video-icon">
                        <a href="/">
                            <img src={Plaqueta} className="img-fluid" alt="Video" />
                        </a>
                        <p>ACCESO TEMPORADAS</p>
                        <p className="small">A todas las temporadas</p>
                    </div>
                    {/* <!-- Segunda columna de imagen --> */}
                    <div className="col text-center chef-icon">
                        <a href="/">
                            <img src={Sombrero} alt="Sombrero" />
                        </a>
                        <p>+300 RECETAS</p>
                        <p className="small">Para aprender</p>
                    </div>
                    {/* <!-- Tercera columna de imagen --> */}
                    <div className="col text-center tray-icon">
                        <a href="/">
                            <img src={Bandeja} className="img-fluid" alt="Bandeja" />
                        </a>
                        <p>LOS MEJORES CHEF</p>
                        <p className="small">Y concursantes</p>
                    </div>
                </div>
                
                <Video 
                
                title="Una receta para chuparte los dedos"
                season="Temporada 10"
                chapter="T5 - E10"
                description="Los aspirantes se enfrentan al desafio de componer un plato que les transporte a sus
                orígenes. En la eliminación deben elaborar un espectacular postre."
                time="3:13:29"
                image={video1}

                />

            </div>

            <div className="container">
                <div className="row mt-5">
                    
                    <Card 
                    
                    title="Último expulsado del programa 10"

                    name="Irene González"
                    phrase="'Lady Bechamel'"
                    description='Una desastrosa salsa Bechamel deja fuera del concurso a Irene Balderrama. A pesar de haber
                    mostrado buena mano con la cocina, la actriz catalana se vio obligada anoche a colgar el
                    delantal del concurso tras el reto fallido de la prueba final de eliminación. "¡A partir de
                    ahora voy a ser Lady Bechamel!", se lamentaba Abril, a medio camino entre las lágrimas de su
                    magnífico sentido del humor.'
                    image={image}

                    name2="Pablo Motos"
                    phrase2="'Me encanta el pitiminí, en la vida y en los platos'"
                    description2='El concursante Pablo Motos se enfrenta al reto de preparar un plato delicioso y refinado
                    para una ocasión especial. Después de las dos horas de trabajo, Pablo presenta su plato con
                    una sonrisa pícara. "Me encanta el pitiminí, en la vida y en los platos", exclama.'
                    image2={image2}
                    />

                    <Card 
                    
                    title="En la cuerda floja"

                    name="Carlos Silvestre, Rocío Molina y Sara Rilo"
                    phrase="'Me encanta el pitiminí, en la vida y en los platos'"
                    description='Una desastrosa prueba de exteriores, lleva a nuestros aspirantes, Carlos, Rocio y Sara a la
                    batalla final, donde se enfrentan con muchos nervios al "Temido" postre. Generar una tarta
                    de chocolate de tres pisos, con ligeros aromas a naranja, hace que los concursantes suden la
                    gota gorda por mantener su puesto en el programa. Entre tanto dulce estos fuertes aspirantes
                    se encuentran en la cuerda floja.'
                    image={image3}

                    name2="Pedro Sánchez, María González"
                    phrase2="'En la Cima del Éxito'"
                    description2='Tras superar desafíos culinarios y demostrar su destreza en la cocina, Pedro, María y Javier 
                    se encuentran en la etapa final del concurso. Una competencia intensa los lleva a enfrentarse al reto final: 
                    preparar un plato gourmet de alta complejidad en un tiempo récord. Con la presión en aumento, estos talentosos 
                    finalistas están al borde de la gloria, saboreando el dulce sabor del éxito mientras se mantienen firmes en 
                    la cima de la competencia.'
                    image2={image4}

                    />

                    <Video 
                    
                    title="Una receta para chuparte los dedos"
                    season="Temporada 10"
                    chapter="T5 - E10"
                    description="Los aspirantes se enfrentan al desafio de componer un plato que les transporte a sus
                    orígenes. En la eliminación deben elaborar un espectacular postre."
                    time="3:13:29"
                    image={video2}

                    />      

                </div>
            </div>

            <div id="slider" className="mb-5 carousel slide-patrocinadores" data-ride="carousel">
                <h2 className="patrocinadores">Patrocinadores</h2>
                <div className="imagenes-patrocinadores">
                    <a href="http://bosch.es" target="_blank" rel="noopener noreferrer"
                        ><img src={sponsor} className="img-fluid" alt="Imagen Grande"
                    /></a>
                    <a href="http://elcorteingles.es" target="_blank" rel="noopener noreferrer"
                        ><img src={sponsor1} className="img-fluid" alt="Imagen Grande"
                    /></a>
                    <a href="http://arcos.es" target="_blank" rel="noopener noreferrer"
                        ><img src={sponsor2} className="img-fluid" alt="Imagen Grande"
                    /></a>
                    <a href="http://lecreuset.es" target="_blank" rel="noopener noreferrer"
                        ><img src={sponsor3} className="img-fluid" alt="Imagen Grande"
                    /></a>
                    <a href="http://aeg.es" target="_blank" rel="noopener noreferrer"
                        ><img src={sponsor4} className="img-fluid" alt="Imagen Grande"
                    /></a>
                </div>
            </div>

        </main>
    )
}

export default Home;