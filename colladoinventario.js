//Carlos Collado Calvo DAM 1_BDD


use('colladoinventario')

// Colección Proveedor
db.Proveedor.insertMany([
  { CIF: '9873490823', Empresa: 'CNA Group', Direccion: 'CALLE PATATA', Ciudad: 'BARCELONA', Telefono: '+34 93 3561182', Email: 'cacafuti@gmail.com' },
  { CIF: '2342398789', Empresa: 'DPLGroup', Direccion: 'CALLE HABICHUELA', Ciudad: 'VALENCIA', Telefono: '+34 96 3561187', Email: 'cacafuto@gmail.com' },
  { CIF: '7236483292', Empresa: 'FerSay', Direccion: 'CALLE GOMINOLA', Ciudad: 'VALENCIA', Telefono: '+34 93 3561184', Email: 'cacafutu@gmail.com' }
  { CIF: '7236412354', Empresa: 'BongoDb', Direccion: 'CALLE FALSA', Ciudad: 'VALENCIA', Telefono: '+34 93 3561234', Email: 'cacafute@gmail.com' }
]);

// Colección Pieza
db.Pieza.insertMany([
  { ID: '15101000', Nombre: 'Motor', Descripcion: 'Grupo motor para campana extractora de cocina', Precio_venta: 95.59 },
  { ID: '15100033', Nombre: 'Botonera', Descripcion: 'Caja de mandos para campana extractora de cocina', Precio_venta: 63.69 },
  { ID: '485189911103', Nombre: 'Condensador', Descripcion: 'Condensador 35 mm - 450V para lavadora', Precio_venta: 6.85 },
  { ID: 'V99I000H1', Nombre: 'Bomba', Descripcion: 'Bomba desagüe EBS2556-0707 para lavadora', Precio_venta: 28.89 },
  { ID: '481946818049', Nombre: 'Burlete', Descripcion: 'Burlete medidas 98.7x57.1 cm para frigorifico combi', Precio_venta: 33.50 },
  { ID: '83040745', Nombre: 'Resistencia', Descripcion: 'Resistencia INFERIOR 900/300w para horno', Precio_venta: 15.25 }
]);

// Colección Pieza_Costo
db.Pieza_Costo.insertMany([
  { CIF_Proveedor: '9873490823', ID_Pieza: '15101000', Precio_costo: 47.40 },
  { CIF_Proveedor: '9873490823', ID_Pieza: '15100033', Precio_costo: 25.78 },
  { CIF_Proveedor: '2342398789', ID_Pieza: '485189911103', Precio_costo: 3.01 },
  { CIF_Proveedor: '2342398789', ID_Pieza: 'V99I000H1', Precio_costo: 12.56 },
  { CIF_Proveedor: '7236483292', ID_Pieza: '481946818049', Precio_costo: 14.97 },
  { CIF_Proveedor: '9873490823', ID_Pieza: '83040745', Precio_costo: 7.46 }
]);

// Colección Ubicacion
db.Ubicacion.insertMany([
  { Estanteria: '1', Estante: 'A' },
  { Estanteria: '1', Estante: 'B' },
  { Estanteria: '2', Estante: 'A' },
  { Estanteria: '2', Estante: 'B' },
  { Estanteria: '3', Estante: 'A' },
  { Estanteria: '4', Estante: 'A' }
]);

// Colección Ubicacion_Pieza
db.Pieza_Ubicacion.insertMany([
  { ID_Pieza: '15101000', EstanteriaUbicacion: '1', EstanteUbicacion: 'A', Stock: 9, Stock_prestado: 1 },
  { ID_Pieza: '15100033', EstanteriaUbicacion: '1', EstanteUbicacion: 'B', Stock: 13, Stock_prestado: 3 },
  { ID_Pieza: '485189911103', EstanteriaUbicacion: '2', EstanteUbicacion: 'A', Stock: 11, Stock_prestado: 0 },
  { ID_Pieza: 'V99I000H1', EstanteriaUbicacion: '2', EstanteUbicacion: 'B', Stock: 2, Stock_prestado: 1 },
  { ID_Pieza: '481946818049', EstanteriaUbicacion: '3', EstanteUbicacion: 'A', Stock: 1, Stock_prestado: 0 },
  { ID_Pieza: '83040745', EstanteriaUbicacion: '4', EstanteUbicacion: 'A', Stock: 6, Stock_prestado: 0 }
]);

// Colección Familia
db.Familia.insertMany([
  { Nombre: 'Campana', Descripcion: 'Extractor de humos activado por un ventilador aspirador, con panel de control y temporizador.' },
  { Nombre: 'Frigorifico', Descripcion: 'Frigorífico combi no frost Total.' },
  { Nombre: 'Lavadora', Descripcion: 'Lavadora carga frontal.' },
  { Nombre: 'Horno', Descripcion: 'Multifunción con HydrocleanECO, Sistema de Limpieza automático, Eficiencia energfética A+' }
]);

// Colección Producto
db.Producto.insertMany([
  { Modelo: 'SYGMA', Marca: 'Cata', Medida: 90, Color: 'Inox', NombreFamilia: 'Campana' },
  { Modelo: 'THALASSA', Marca: 'Cata', Medida: 60, Color: 'BLACK', NombreFamilia: 'Campana' },
  { Modelo: '4FE-8814', Marca: 'Fagor', Medida: null, Color: null, NombreFamilia: 'Lavadora' },
  { Modelo: 'W19l MO1L Combi', Marca: 'Whirlpool', Medida: null, Color: 'Inox', NombreFamilia: 'Frigorifico' },
  { Modelo: 'HCB 6535', Marca: 'Teka', Medida: 60, Color: 'Inox', NombreFamilia: 'Horno' }
]);

// Colección Pieza_pertenece_Producto
db.Pieza_pertenece_Producto.insertMany([
  { ID_Pieza: '15101000', ModeloProducto: 'SYGMA', MarcaProducto: 'Cata' },
  { ID_Pieza: '15100033', ModeloProducto: 'THALASSA', MarcaProducto: 'Cata' },
  { ID_Pieza: '485189911103', ModeloProducto: '4FE-8814', MarcaProducto: 'Fagor' },
  { ID_Pieza: 'V99I000H1', ModeloProducto: '4FE-8814', MarcaProducto: 'Fagor' },
  { ID_Pieza: '481946818049', ModeloProducto: 'W19l MO1L Combi', MarcaProducto: 'Whirlpool' },
  { ID_Pieza: '83040745', ModeloProducto: 'HCB 6535', MarcaProducto: 'Teka' }
]);
