AOS.init();
// You can also pass an optional settings object
// below listed default settings
AOS.init({
  
  // Settings that can be overridden on per-element basis, by `data-aos-*` attributes:
  offset: 120, // offset (in px) from the original trigger point
  delay: 0, // values from 0 to 3000, with step 50ms
  duration: 700, // values from 0 to 3000, with step 50ms
  easing: 'ease', // default easing for AOS animations
  once: false, // whether animation should happen only once - while scrolling down
  mirror: false, // whether elements should animate out while scrolling past them
  anchorPlacement: 'top-bottom', // defines which position of the element regarding to window should trigger the animation

});
/* emailjs*/
    (function() {
        emailjs.init('w9KEeTkdztGG_h94c'); // Reemplaza 'w9KEeTkdztGG_h94c' con tu ID de usuario de EmailJS
    })();

    document.getElementById('contact-form').addEventListener('submit', function(event) {
        event.preventDefault();

        const btn = document.getElementById('button');
        btn.textContent = 'Enviando...';

        const serviceID = 'default_service';
        const templateID = 'template_gih8q2f';

        emailjs.sendForm(serviceID, templateID, this)
            .then(() => {
                btn.textContent = 'Enviar Mensaje';
                alert('Mensaje enviado!');
            }, (err) => {
                btn.textContent = 'Enviar Mensaje';
                alert(JSON.stringify(err));
            });
    });


    function toggleDescripcion(index) {
        var descripcionCorta = document.getElementById('descripcion-corta-' + index);
        var descripcionLarga = document.getElementById('descripcion-larga-' + index);
        var toggleLink = document.getElementById('toggle-link-' + index);

        if (descripcionCorta.classList.contains('d-none')) {
            descripcionCorta.classList.remove('d-none');
            descripcionLarga.classList.add('d-none');
            toggleLink.textContent = 'Ver más';
        } else {
            descripcionCorta.classList.add('d-none');
            descripcionLarga.classList.remove('d-none');
            toggleLink.textContent = 'Ver menos';
        }
    }

//carrito
    //Variables
const carrito = document.getElementById('carrito'),

    listapeliculas = document.getElementById('#peliculas,#series,#Recomendados'),
contenedorCarrito = document.querySelector('.buy-card .lista_de_peliculas'),
vaciarCarritoBtn = document.querySelector('#vaciar_carrito');

let articulosCarrito = [];

registrarEventsListeners()

function registrarEventsListeners() {
//Cuando yo le de click a "agregar al carrito de compras"
listaPeliculas.addEventListener('click', agregarPelicula);

//Eliminar curso del carrito
carrito.addEventListener('click', eliminarPelicula);

//Vaciar el carrito
vaciarCarritoBtn.addEventListener('click', e => {
    articulosCarrito = [];
    limpiarHTML()
})
}

function agregarPelicula(e) {
    if (e.target.classList.contains("agregar-carrito")) {
        const PeliculaSeleccionada = e.target.parentElement.parentElement;
        leerInfo(PeliculaSeleccionada);
    }
}


function eliminarPelicula(e) {
    if(e.target.classList.contains("borrar-Pelicula")) {
        const peliculaId = e.target.getAttribute('data-id');

        //Eliminar del arreglo del articulosCarrito por el data-id
        articulosCarrito = articulosCarrito.filter(pelicula => pelicula.id !== peliculaId)

        carritoHTML()
    }
}

//Leer el contenido de nuestro HTML al que le dimos click y extrae la info del curso
function leerInfo(Pelicula) {
    //Crear un objeto con el contenido del curso actual
    const infoCurso = {
        imagen : Pelicula.querySelector('img').src,
        titulo : Pelicula.querySelector('h3').textContent,
        precio : Pelicula.querySelector('.descuento').textContent,
        cantidad : 1
    }

//Revisa si un elemento ya existe en el carrito
const existe = articulosCarrito.some(pelicula => pelicula.id === infopelicula.id);

if (existe) {
    //Actualizar la cantidad
    const pelicula = articulosCarrito.map(pelicula => {
        if (pelicula.id === infopelicula.id) {
            pelicula.cantidad++;
            return pelicula;
        } else {
            return pelicula;
        }
    });

    [...articulosCarrito, infopelicula]
} else {
    //Agregamos elementos al carrito de compras
    articulosCarrito = [...articulosCarrito, infopelicula]
}

carritoHTML()
}
//Muestra el carrito en el HTML
function carritoHTML() {
    limpiarHTML();
    //Recorre el carrito de compras y genera el HTML
    articulosCarrito.forEach(pelicula => {
        const fila = document.createElement('div');
        fila.innerHTML = `
            <img src="${pelicula.imagen}" ></img>
            <p>${pelicula.titulo}</p>
            <p>${pelicula.precio}</p>
            <p>${pelicula.cantidad}</p>
            <p><span class="borrarPelicula" data-id=${pelicula.id}>X</span></p>
        `;

        contenedorCarrito.appendChild(fila);
    });
}

//Elimina los cursos de la lista_de_cursos
function limpiarHTML() {
    while (contenedorCarrito.firstChild) {
        contenedorCarrito.removeChild(contenedorCarrito.firstChild);
    }
}
