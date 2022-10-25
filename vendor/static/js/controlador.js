/**
 * Cambia la cantidad de un producto en el carrito
 * @param {int} id: PK del registro del produto en el carrito 
 */
 function cambiarCantidad(id) {
    let cantidad = document.getElementById('cantidad_'+id).value;
    let valorUnit = document.getElementById('cantidad_'+id).dataset.preciou;

    let url = "http://localhost:8000/productos/cambiarCantidad/";
    let datos = {
        'id': id,
        'cantidad': cantidad
    };

    let total = parseFloat(cantidad) * parseFloat(valorUnit);
    document.getElementById('total_'+id).innerText = '$' + total;
    mensajeAjax(url, datos, cambiarCantidadResp)    
}

function cambiarCantidadResp(data) {
    document.getElementById('subtotal').innerText = '$' + data['subtotal'];
    document.getElementById('iva').innerText = '$' + data['iva'];
    document.getElementById('envio').innerText = '$' + data['envio'];
    document.getElementById('total').innerText = '$' + data['total'];
 
}

//************ FUNCIONES AUXILIARES ************************************************************** */
/**
 * Consulta AJAX al servidor por método POST
 * @param {*} urlserver :Direccion de envio
 * @param {*} datos     :Data en formato JavaScript object
 * @param {*} callBackFunction : Funcion de retorno
 */
 function mensajeAjax(urlserver, datos, callBackFunction) {

    const csrftoken = getCookie('csrftoken');
    fetch(urlserver, {
        method: 'POST',
        credentials: 'same-origin',
        headers: {
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify(datos) //JavaScript object of data to POST
    })
        .then(response => response.json())  //Convierte la respuesta JSON en data
        .then(data => {
            //mostrarAviso(data)
            callBackFunction(data)
        })
        .catch((error) => {
            console.error('Error:', JSON.stringify(error));
        });
}


/**
 * @param {*} name Nombre de la cookie
 * @returns el cvontenido de la cookie
 */
 function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
