// test_carga_motores.js
// Archivo de prueba para verificar carga de motores en Fontanero Virtual

console.log("Iniciando test de carga de motores...");

try {
    if (typeof MotorV3 !== "undefined") console.log("MotorV3 cargado correctamente");
    else console.log("MotorV3 no cargado");

    if (typeof MotorV4 !== "undefined") console.log("MotorV4 cargado correctamente");
    else console.log("MotorV4 no cargado");

    if (typeof MotorVendedor !== "undefined") console.log("MotorVendedor cargado correctamente");
    else console.log("MotorVendedor no cargado");

} catch (e) {
    console.error("Error durante la carga de motores:", e);
}

console.log("Test de carga de motores finalizado.");
